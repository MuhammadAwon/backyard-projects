# How to change the perspective of an image

import cv2 as cv
import numpy as np

img = cv.imread('resources/tilted_image.png')
print(img.shape)

# Define points
point1 = np.float32([[233, 196], [82, 471], [522, 169], [715, 482]])
width = 800
height = 900
point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv.getPerspectiveTransform(point1, point2)

output_img = cv.warpPerspective(img, matrix, (width, height))

cv.imshow('Original', img)
cv.imshow('Transformed', output_img)
cv.waitKey(0)
cv.destroyAllWindows()