# How to capture a webcam inside python

# Step 1: import libraries
import cv2 as cv
import numpy as np

# Step 2: read the frames from camera
cap = cv.VideoCapture(1)  # webcam# 0 or 1 or 2 so on..

# Step 3: display capture
# Read cam until the end
while (cap.isOpened()):
    # Capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # Display frame
        cv.imshow("Frame", frame)
        # Quit with the 'q' key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

# Step 4: Close windows
cap.release()
cv.destroyAllWindows()