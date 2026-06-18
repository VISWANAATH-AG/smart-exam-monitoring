import cv2
import mediapipe as mp
import time

# MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

away_start = None

print("Eye Tracking Started")
print("Press Q to Quit")

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    status = "Looking Forward"

    if results.multi_face_landmarks:

        face_landmarks = results.multi_face_landmarks[0]

        left_eye = face_landmarks.landmark[33]
        right_eye = face_landmarks.landmark[263]

        nose = face_landmarks.landmark[1]

        if nose.x < 0.40:
            status = "Looking Left"

        elif nose.x > 0.60:
            status = "Looking Right"

        else:
            status = "Looking Forward"

        if status != "Looking Forward":

            if away_start is None:
                away_start = time.time()

            away_time = time.time() - away_start

            if away_time > 5:
                cv2.putText(
                    frame,
                    "SUSPICIOUS BEHAVIOR",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

        else:
            away_start = None

    cv2.putText(
        frame,
        status,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Eye Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()