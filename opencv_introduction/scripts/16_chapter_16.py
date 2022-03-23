# Save HD recording of cam streaming
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)

# Create function to set resolution (For example, HD: 1280x720)
def set_resolution(width, height):
    cap.set(3, width) 
    cap.set(4, height)

# Get input width and height from user
width = int(input('Enter width size: '))
height = int(input('Enter height size: '))
# Call set_resolution function
set_resolution(width, height)

# Video writing format, codec, video writer object and file object
# Frame resolution size
frame_height = int(cap.get(3))
frame_width = int(cap.get(4))
frame_size = (frame_height, frame_width)

# Save video
out = cv.VideoWriter('resources/new_cam_video.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, frame_size)

while True:
    (ret, frame) = cap.read()
    # Run video in player
    if ret == True:
        out.write(frame)
        cv.imshow('frame', frame)
        # Quit with the 'q' key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()