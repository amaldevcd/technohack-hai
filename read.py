#individual program to recognize the person ( different for different person)
import numpy as np
import cv2
import pickle
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer =cv2.face.LBPHFaceRecognizer_create()
recognizer.read("model.yml")



labels={"person_name":1}
with open("labels.pickle", 'rb') as f:
    real_labels=pickle.load(f)
    labels = {v:k for k,v in real_labels.items()}

def most_frequent(list):
    return max(set(list), key = list.count)
list =[]

capture_duration = 10

vid =cv2.VideoCapture("pics/vid3.mp4")

start_time = time.time()

while(int(time.time() - start_time) < capture_duration):
    isTrue, frame=vid.read()
    count=0
    if count>10:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for(x,y,w,h) in faces:
        # print(x,y,w,h)
        roi_gray =gray[y:y+h,x:x+w]

        id_,conf =recognizer.predict(roi_gray)
        if conf<90:
            # print(id_)
            # print(labels[id_])
            list.append(labels[id_])
            count+=1
        else:
            print('\a')
            list.append('\a')
        color= (255,0,0)
        stroke = 2
        x_end_cord= x+w
        y_end_cord= y+h
        cv2.rectangle(frame,(x,y),(x_end_cord,y_end_cord),color,stroke)
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
if(most_frequent(list))=="elon-musk":
    print(most_frequent(list), " is present")
else:
    print("elon-musk is absent")

vid.release()
cv2.destroyAllWindows()