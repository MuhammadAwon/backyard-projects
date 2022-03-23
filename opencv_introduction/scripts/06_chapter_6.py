# Read a video
import cv2 as cv

cap = cv.VideoCapture('resources/night_sky.mp4')

# Indicator
if (cap.isOpened() == False):
    print('error in reading video')

# Read and play video
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Video', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()