# Convert video into gray and black&white
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

while True:
    (ret, frame) = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (tresh, binary_frame) = cv.threshold(gray_frame, 127, 225, cv.THRESH_BINARY)


    cv.imshow("OriginalCam", frame)
    cv.imshow("GrayCam", gray_frame)
    cv.imshow("BinaryCam", binary_frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()