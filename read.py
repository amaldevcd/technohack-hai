import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vid =cv2.VideoCapture(0)

while(True):
    isTrue, frame=vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for(x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray =gray[y:y+h,x:x+w]
        color= (255,0,0)
        stroke = 2
        x_end_cord= x+w
        y_end_cord= y+h
        cv2.rectangle(frame,(x,y),(x_end_cord,y_end_cord),color,stroke)
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()