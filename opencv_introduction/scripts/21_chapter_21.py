# How to detect specific colors of an image
import cv2 as cv
from cv2 import imwrite
import numpy as np

# image path
path = 'resources/resized_salmon.jpg'

# define function for slider
def slider():
    pass

# create bar window
cv.namedWindow('Bars')
cv.resizeWindow('Bars', 900,300)

# create hue slider on window
cv.createTrackbar('Hue Min', 'Bars', 0,179, slider)
cv.createTrackbar('Hue Max', 'Bars', 179,179, slider)
# create saturation slider on window
cv.createTrackbar('Sat Min', 'Bars', 0,255, slider)
cv.createTrackbar('Sat Max', 'Bars', 255,255, slider)
# create value slider on window
cv.createTrackbar('Val Min', 'Bars', 0,255, slider)
cv.createTrackbar('Val Max', 'Bars', 255,255, slider)

# read image
img = cv.imread(path)
# convert image to hsv
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)


while True:
    # read image
    img = cv.imread(path)
    # convert image to hsv
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # track min & max hue
    hue_min = cv.getTrackbarPos('Hue Min', 'Bars')
    hue_max = cv.getTrackbarPos('Hue Max', 'Bars')
    # track min & max saturation
    sat_min = cv.getTrackbarPos('Sat Min', 'Bars')
    sat_max = cv.getTrackbarPos('Sat Max', 'Bars')
    # track min & max value
    val_min = cv.getTrackbarPos('Val Min', 'Bars')
    val_max = cv.getTrackbarPos('Val Max', 'Bars')
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

    # see these changes inside an image
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img, img, mask=mask_img)


    # cv.imshow('Original', img)
    # cv.imshow('HSV', hsv_img)
    cv.imshow('Mask', mask_img)
    cv.imshow('Final Output', out_img)

    cv.imwrite('resources/salmonhsv.jpg', mask_img)
    cv.imwrite('resources/salmonmask.jpg', mask_img)
    cv.imwrite('resources/salmonoutput.jpg', out_img)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cv.destroyAllWindows()