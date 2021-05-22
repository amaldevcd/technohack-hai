import os
import numpy as np
from PIL import Image
import cv2
import pickle
BASE_DIR =os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "pics/vid3.mp4")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer =cv2.face.LBPHFaceRecognizer_create()
current_id=0
label_ids={}
y_label=[]
x_train=[]

for root,dirs, files in os.walk (image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root,file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","-").lower()
            # print(label,path)
            if label in label_ids:
                pass
            else:
                label_ids[label]=current_id
                current_id+=1
            
            id_=label_ids[label]

            pil_image =Image.open(path).convert("L")
            image_array = np.array(pil_image, "uint8")
            # print(image_array)
            faces = face_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=5)
            for(x,y,w,h) in faces:
                roi =image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_label.append(id_)



with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_label))
recognizer.save("model.yml")