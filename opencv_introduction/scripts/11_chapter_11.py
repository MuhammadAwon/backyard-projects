# Writing videos from cam
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

# Video writing format, codec, video writer object and file object
# Frame resolution size
frame_height = 640
frame_width = 480
frame_size = (frame_height, frame_width)

out = cv.VideoWriter('resources/cam_video.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, frame_size)

while True:
    (ret, frame) = cap.read()

    # Run video in player
    if ret == True:
        # Resize frames of the video
        b = cv.resize(frame, frame_size, fx=0, fy=0, interpolation=cv.INTER_CUBIC)
        out.write(b)
        cv.imshow('frame', b)
        # Quit with the 'q' key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()