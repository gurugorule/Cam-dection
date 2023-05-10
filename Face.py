import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpface = mp.solutions.face_detection
face = mpface.FaceDetection()
mpDraw = mp.solutions.drawing_utils

ptime = 0
ctime = 0
while True:
    success, img = cap.read()
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face.process(img_RGB)
    if results.detections:
        for id, dectections in enumerate(results.detections):
            # mpDraw.draw_detection(img, dectections)
            boxc = dectections.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            box = int(boxc.xmin*iw),int(boxc.ymin*ih), int(boxc.width*iw), int(boxc.height*ih)
            cv2.rectangle(img, box, (255, 0, 255), 2)
            cv2.putText(img, f"{str(int(dectections.score[0] * 100))}%", (box[0], box[1]-20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
