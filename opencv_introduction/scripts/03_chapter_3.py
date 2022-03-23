# Convert image into grayscale
# Import library
import cv2 as cv
from cv2 import cvtColor

img = cv.imread('./resources/space.jpg')
img = cv.resize(img, (600, 400))

# Conversion
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)

# Display image
cv.imshow('Pehli Image', img)
cv.imshow('Gray Image', gray_img)

# Delay code
cv.waitKey(0)
cv.destroyAllWindows()