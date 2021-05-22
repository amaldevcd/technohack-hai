import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer =cv2.face.LBPHFaceRecognizer_create()
recognizer.read("model.yml")

labels={"person_name":1}
with open("labels.pickle", 'rb') as f:
    real_labels=pickle.load(f)
    labels = {v:k for k,v in real_labels.items()}


vid =cv2.VideoCapture("pics/vid2.mp4")

while(True):
    isTrue, frame=vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for(x,y,w,h) in faces:
        # print(x,y,w,h)
        roi_gray =gray[y:y+h,x:x+w]

        id_,conf =recognizer.predict(roi_gray)
        if conf<100 :
            # print(id_)
            print(labels[id_])
        else:
            print('\a')
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