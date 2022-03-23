# Convert video to gray and black & white
import cv2 as cv

cap = cv.VideoCapture('resources/night_sky.mp4')

while True:
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (tresh, binary) = cv.threshold(grayframe, 127, 225, cv.THRESH_BINARY)

    # Run video
    if ret == True:
        cv.imshow('Video', binary)
        # Quit with the 'q' key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()