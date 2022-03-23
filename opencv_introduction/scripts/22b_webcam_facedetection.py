# Face detection in webcam 
import cv2 as cv

# import cascade classifier
face_cascade = cv.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

# capture video from webcam
video_capture = cv.VideoCapture(1)

while True:
    # capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1,
                                          minNeighbors=5,
                                          minSize=(30,30),
                                          flags=cv.CASCADE_SCALE_IMAGE)

    # draw a rectangle around the faces
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,225,0), 2)
    
    # display the resulting frame
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break

# release the capture when everything is done
video_capture.release()
cv.destroyAllWindows()