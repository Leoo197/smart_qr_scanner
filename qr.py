import cv2 as cv
import webbrowser

capture = cv.VideoCapture(0)

detector = cv.QRCodeDetector()

print("Starting camera... Hold up a QR code!")
print("Press 'q' to quit")

while True:
    success, frame = capture.read()

    if not success:
        break
    
    data, bbox, _ = detector.detectAndDecode(frame)

    if bbox is not None and data:
        print(f"Detected: {data}")
    
        bbox = bbox[0].astype(int)
        for i in range(len(bbox)):
            cv.line(frame, tuple(bbox[i]), tuple(bbox[(i+1) % len(bbox)]), (255, 161, 22), 5)

        cv.putText(frame, data, (bbox[0][0], bbox[0][1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (153, 72, 236), 2)

    cv.imshow('OpenCV Native Scanner', frame)
    if data.startswith("http"):
            print("Opening link in browser...")
            webbrowser.open(data)
            break

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
print("Scanner closed")


