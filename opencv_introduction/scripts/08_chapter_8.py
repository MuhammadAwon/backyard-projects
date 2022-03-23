# Write video to gray
import cv2 as cv

cap = cv.VideoCapture('resources/night_sky.mp4')

# Video writing format, codec, video writer object and file objec
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('resources/gray_sky_night.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while True:
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Run video in player
    if ret == True:
        out.write(grayframe)
        cv.imshow('Video', grayframe)
        # Quit with the 'q' key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()