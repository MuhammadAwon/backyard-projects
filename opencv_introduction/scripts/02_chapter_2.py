# Resizing the image and displaying it
# Import library
import cv2 as cv

img = cv.imread('./resources/space.jpg')
img1 = cv.resize(img, (500, 500))

cv.imshow('Pehli Image', img)
cv.imshow('Dosari Image', img1)

cv.waitKey(0)
cv.destroyAllWindows()