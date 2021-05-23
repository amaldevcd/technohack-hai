import cv2 
import time
import os
import time

capture_duration= 15

print("Enter your name :")
name = input()
print("_________CAPTURING YOUR PICTURE: LOOK INTO THE VARIOUS PARTS OF SCREEN___________")
dir_path = os.path.dirname(os.path.realpath(__file__))
img_dir = os.path.join(dir_path,"pics")
path  = os.path.join(img_dir,name)
os.mkdir(path)

camera = cv2.VideoCapture(0)
count = 1

start_time = time.time()

while(int(time.time() - start_time) < capture_duration):
 	ret, image = camera.read()
 	cv2.imwrite(os.path.join(path,str(count)+'.jpg'), image)
 	time.sleep(3)
 	count+=1
print("Capturing ended sucessfully")
camera.release()
cv2.destroyAllWindows()
