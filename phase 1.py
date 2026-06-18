from ultralytics import YOLO
import cv2
import os
from datetime import datetime
import pandas as pd

# Load YOLOv8 Model
model = YOLO("yolov8n.pt")

# Create evidence folder
os.makedirs("evidence", exist_ok=True)

# Create CSV file if not exists
if not os.path.exists("violations.csv"):
    df = pd.DataFrame(columns=["Time", "Violation", "Image"])
    df.to_csv("violations.csv", index=False)

# Open Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not found!")
    exit()

print("===================================")
print(" SMART EXAM MONITORING SYSTEM")
print(" Mobile Detection Started")
print(" Press Q to Quit")
print("===================================")

phone_counter = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    phone_detected = False

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])

            confidence = float(box.conf[0])

            label = model.names[cls]

            # Detect only mobile phone
            if label == "cell phone" and confidence > 0.50:

                phone_detected = True

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"PHONE {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

    if phone_detected:
        phone_counter += 1
    else:
        phone_counter = 0

    # Save evidence only if phone appears for 10 frames
    if phone_counter >= 10:

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        image_path = f"evidence/{timestamp}.jpg"

        cv2.imwrite(image_path, frame)

        log = pd.read_csv("violations.csv")

        log.loc[len(log)] = [
            timestamp,
            "Mobile Phone Detected",
            image_path
        ]

        log.to_csv("violations.csv", index=False)

        print(f"Violation Detected at {timestamp}")

        phone_counter = 0

    cv2.imshow("Smart Exam Monitoring - Mobile Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()