import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
ptime = 0
ctime = 0
while True:
    success, img = cap.read()
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img_RGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img , results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)