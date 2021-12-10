import cv2
import os
from helpers import is_path


vid_cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = 1

count = 0
is_path("training_data/")

while(True):
    ret, image_frame = vid_cam.read()
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)

    if ret:
        count += 1
        cv2.imwrite("training_data/Person." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.putText(image_frame, f'{count}', (250,250), cv2.FONT_HERSHEY_COMPLEX, 1, (250,0,0), 3)
        cv2.imshow('frame', image_frame)

    if cv2.waitKey(1) == ord('q'):
        break

    elif count>1000:
        break

vid_cam.release()
cv2.destroyAllWindows()
