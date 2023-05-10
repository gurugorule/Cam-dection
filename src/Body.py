import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

mpface = mp.solutions.face_detection
face = mpface.FaceDetection()
mpDraw = mp.solutions.drawing_utils

ptime = 0
ctime = 0
while True:
    success, img = cap.read()
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results1 = hands.process(img_RGB)
    results2 = pose.process(img_RGB)
    results3 = face.process(img_RGB)

    if results1.multi_hand_landmarks:
        for handlms in results1.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 0 or id == 4:
                    cv2.circle(img, (cx, cy), 15, (200, 200, 200), cv2.FILLED)
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

    if results2.pose_landmarks:
        mpDraw.draw_landmarks(img , results2.pose_landmarks, mpPose.POSE_CONNECTIONS)

    if results3.detections:
        for id, dectections in enumerate(results3.detections):
            # mpDraw.draw_detection(img, dectections)
            boxc = dectections.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            box = int(boxc.xmin * iw), int(boxc.ymin * ih), int(boxc.width * iw), int(boxc.height * ih)
            cv2.rectangle(img, box, (255, 0, 255), 2)
            cv2.putText(img, f"{str(int(dectections.score[0] * 100))}%", (box[0], box[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                        1, (255, 0, 255), 2)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
