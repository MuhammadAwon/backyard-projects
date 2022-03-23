# Basic functions or manipulations in opencv

import cv2 as cv
import numpy as np

# Read image
img = cv.imread('resources/chef.jpg')

# Resize image
resized_img = cv.resize(img, (450, 250))

# Gray image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Black & white image
(tresh, bitonal_img) = cv.threshold(gray_img, 127, 225, cv.THRESH_BINARY)

# Blurred image
blurr_img = cv.GaussianBlur(img, (7,7), 0) # 7x7 is kernel size that has to be odd

# Edge detection
edge_img = cv.Canny(img, 47, 47)

# thickness of lines (has to be edge_img)
mat_kernel = np.ones((7,7), np.uint8)
dilated_img = cv.dilate(edge_img, mat_kernel, iterations=1)

# Make thinner outline (opposite to the function above)
ero_img = cv.erode(dilated_img, mat_kernel)

# Crop image using numpy
print(f'The size of our image is: {img.shape}')
cropped_img = img[0:500, 300:650]


cv.imshow('Original', img)
cv.imshow('Resized', resized_img)
cv.imshow('Gray', gray_img)
cv.imshow('B&W', bitonal_img)
cv.imshow('Blurr', blurr_img)
cv.imshow('Edge', edge_img)
cv.imshow('Dilated', dilated_img)
cv.imshow('Erosion', ero_img)
cv.imshow('Cropped', cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()
