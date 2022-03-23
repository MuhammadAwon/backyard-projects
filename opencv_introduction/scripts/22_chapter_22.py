# Face detection in image
import cv2 as cv

# import cascade classifier
face_cascade = cv.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
# read image
img = cv.imread('resources/face.jpg')
# convert image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)
print(faces)

# draw rectangle around face
for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv.imshow('image', img)
cv.imwrite('resources/face1.png', img)
cv.waitKey(0)
cv.destroyAllWindows()