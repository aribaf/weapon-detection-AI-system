import cv2
import cvzone
import math
import time
import pygame
from twilio.rest import Client
import requests
from ultralytics import YOLO

# Initialize pygame
pygame.init()

# Twilio credentials (replace with your own)
ACCOUNT_SID = 'AC503924e744dde88ce6642c1ebbbcb973'
AUTH_TOKEN = 'a8348ec4ad64fe575c4a65fd89a7ae71'
TWILIO_PHONE_NUMBER = '+15413667832'
USER_PHONE_NUMBER = '+923254499176'
# Imgur credentials (replace with your own)
IMGUR_CLIENT_ID = '8ec89bffb051925'

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def upload_image_to_imgur(image_path):
    """Uploads an image to Imgur and returns the image URL"""
    headers = {
        'Authorization': f'Client-ID {IMGUR_CLIENT_ID}'
    }
    with open(image_path, 'rb') as img_file:
        response = requests.post(
            'https://api.imgur.com/3/upload',
            headers=headers,
            files={'image': img_file}
        )
    data = response.json()
    if data['success']:
        return data['data']['link']  # Return the image URL
    else:
        print(f"Failed to upload image to Imgur: {data['data']['error']}")
        return None

def send_sms_notification(image_url):
    """Sends SMS with the Imgur image URL"""
    message = client.messages.create(
        body="Alert: Weapon detected! Check the attached image.",
        from_='+15413667832',
        to='+923254499176',
    )
    print(f"SMS sent: {message.sid}")

# Set up the screen (window size to match webcam capture size)
screen = pygame.display.set_mode((640, 480))

cap = cv2.VideoCapture(0)  # For Webcam
cap.set(3, 640)
cap.set(4, 480)

model = YOLO("../py-weight/yolov8n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

prev_frame_time = 0
new_frame_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cap.release()
            exit()

    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream=True)
    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if (currentClass == "person" or currentClass == "knife") and conf > 0.1:
                cvzone.cornerRect(img, (x1, y1, w, h))
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=0.8, thickness=1,
                                   offset=3)
            
            if currentClass == "knife":
                print(f"Weapon detected at {x1, y1}!")

                # Capture the image
                img_name = "weapon_detected.jpg"
                if cv2.imwrite(img_name, img):
                    print(f"Image saved as {img_name}")
                else:
                    print("Failed to save image")

                # Upload image to Imgur and get URL
                img_url = upload_image_to_imgur(img_name)
                if img_url:
                    # Send SMS with the image URL
                    send_sms_notification(img_url)

    # Calculate FPS
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(f"FPS: {fps}")

    # Convert the image to a format suitable for pygame (RGB)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Create a pygame surface from the image
    img_surface = pygame.surfarray.make_surface(img_rgb)

    # Display the image
    screen.blit(img_surface, (0, 0))
    pygame.display.update()
