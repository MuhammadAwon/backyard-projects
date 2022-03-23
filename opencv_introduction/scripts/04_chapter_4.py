# Convert Image into black & white
import cv2 as cv

img = cv.imread('resources/space.jpg')
img = cv.resize(img, (400, 200))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(tresh, binary) = cv.threshold(gray, 127, 225, cv.THRESH_BINARY)

cv.imshow('orignal', img)
cv.imshow('gray', gray)
cv.imshow('black and white', binary)
cv.waitKey(0)
cv.destroyAllWindows()