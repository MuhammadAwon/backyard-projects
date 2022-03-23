# Joining two images

import cv2 as cv
from cv2 import imwrite
import numpy as np

img = cv.imread('resources/resized_img.jpg')

# Stocking same image

# horizontal stacking
hor_img = np.hstack((img, img))

# Vertical stacking
ver_img = np.vstack((img, img))


# cv.imshow('Horizontal', hor_img)
cv.imshow('Vertical', ver_img)
cv.waitKey(0)
cv.destroyAllWindows()