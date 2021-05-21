import numpy as np
import cv2

vid =cv2.VideoCapture(0)

while(True):
    isTrue, frame=vid.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()