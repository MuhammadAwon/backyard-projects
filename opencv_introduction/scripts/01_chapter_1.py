# Reading and displaying an image
# Import library
import cv2 as cv

img = cv.imread('./resources/space.jpg')

cv.imshow('Pehli Image', img)
cv.waitKey(0)