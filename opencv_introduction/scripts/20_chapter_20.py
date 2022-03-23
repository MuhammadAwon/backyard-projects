# Split video into frames (image sequence)
import cv2 as cv

cap = cv.VideoCapture('resources/grilled_steaks.mp4')

frameNum = 0

while True:
    ret, frame = cap.read()
    if ret:
        cv.imwrite(f'resources/frames/frame_{frameNum}.jpg', frame)
    else:
        break
    frameNum += 1 # increment frames count

cap.release()
print('Frames count completed!!')