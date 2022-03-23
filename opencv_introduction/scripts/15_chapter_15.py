# Resolution of cam
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

# Create function to set resolution (For example, HD: 1280x720)
def set_resolution(width, height):
    cap.set(3, width) 
    cap.set(4, height)

width = int(input('Enter width size: '))
height = int(input('Enter height size: '))

set_resolution(width, height)



while True:
    ret, frame = cap.read()
    if ret==True:
        cv.imshow('Camera view', frame)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()