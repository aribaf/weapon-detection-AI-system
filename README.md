# Weapon Detection AI System
Real-Time CCTV Monitoring using YOLOv8 and Python

Overview:
This advanced weapon detection AI system is designed for CCTV cameras, utilizing a modified YOLOv8 model with Python. It detects weapons, such as knives, in real-time and sends instant alerts to security personnel through SMS notifications, ensuring rapid response to potential threats.

Key Features:
Real-Time Detection: Leverages a fine-tuned YOLOv8 model for accurate and efficient weapon detection.
Instant Alerts: Integrates Twilio API to send SMS notifications with an image link via Imgur, enabling quick action by security personnel.
Tech Stack: Python, OpenCV, PyTorch, YOLOv8, Twilio API, and Imgur API.
User-Friendly Display: Utilizes Pygame for live video feed visualization.
Security & Privacy Considerations:
Environment Variables: Sensitive credentials (Twilio and Imgur API keys) are recommended to be stored as environment variables for enhanced security.
Real-Time Notification: Immediate alerts help minimize potential threats and enhance overall security measures.
Importance in Security:
Proactively identifies weapons, ensuring quick response and preventing potential security breaches.
Reduces reliance on manual monitoring by automating weapon detection and alerting processes.
This project showcases an innovative approach to surveillance and security, utilizing cutting-edge AI technology to detect weapons in real-time and alert relevant authorities swiftly.









- Python: Programming language used for implementing the system and integrating various components.
- OpenCV (cv2): Library employed for accessing the CCTV camera feed and capturing frames.
- PyTorch: Deep learning framework utilized to load and utilize the modified YOLOv8 model.
- Modified YOLOv8 Weights and Configuration Files: Fine-tuned or transfer-learned weights and configuration files specifically designed to identify dangerous objects like knives.

Importance in Security:
The implementation of an object detection and alarming system, as presented in our project, holds great significance in enhancing security in society. By deploying such systems in public areas, high-risk locations, or critical infrastructure, we can:

1. Proactively Identify Threats: The system's real-time object detection capabilities enable proactive identification of dangerous objects, allowing security personnel to swiftly respond and mitigate potential threats.

2. Prompt Notification: The immediate notification sent to nearby law enforcement officers or security guards ensures quick response times, minimizing the potential for mishaps or security breaches.

3. Prevention of Crime: By deterring individuals from carrying dangerous objects and enabling rapid intervention, the system acts as a deterrent against criminal activities, contributing to a safer environment for society.

4. Enhanced Surveillance: Continuous monitoring of CCTV camera feeds using automated detection systems reduces reliance on manual monitoring, enabling security personnel to focus on critical tasks while minimizing human errors.

In conclusion, our project presents an innovative approach to security enhancement by utilizing a modified version of the YOLOv8 model and Python. The system's ability to detect dangerous objects, such as knives, in real-time and raise alarms promptly ensures swift response and prevention of potential mishaps or security breaches. Such advanced object detection and alarming systems play a crucial role in bolstering security measures and fostering a safer society.
