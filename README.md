# Smart QR Scanner

A real-time, lightweight computer vision utility that detects, decodes, and tracks QR codes using your computer's webcam. 

This project bypasses the need for heavy third-party decoding libraries by utilizing OpenCV's native QR Code Detector, resulting in a faster, crash-resistant application.

## Features
* **Real-Time Detection:** Captures and processes live video feeds at 30+ FPS.
* **Dynamic Visual Tracking:** Automatically calculates coordinates and draws a precision bounding box around detected QR codes.
* **Smart URL Routing:** Recognizes web addresses and automatically routes them to your default web browser.

## Tech Stack
* **Language:** Python
* **Core Library:** OpenCV (`cv2`)
* **Built-in Modules:** `webbrowser`

## How to Run This Project Locally

**1. Clone the repository**
Open your terminal and run:
`git clone https://github.com/Leoo197/smart-qr-scanner.git`

**2. Navigate into the folder**
`cd smart-qr-scanner`

**3. Install dependencies**
Make sure you have Python installed, then install the OpenCV library:
`pip install opencv-python`

**4. Run the scanner**
`python qr.py`

*(Note: Press the `q` key at any time while the window is active to safely close the camera and exit the program).*