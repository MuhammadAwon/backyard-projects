# Find coordinates of an image or video
# Find BGR color codes from an image

# Step-1: Import libraries
import cv2 as cv
import numpy as np

# Step-2: Define a function
def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        # left mouse click
        print(x, '', y)
        # how to display coordinates on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' + str(y), (x, y), font, 1, (116,150,234), thickness=2)
        # show the text on image
        cv.imshow('image', img)

    # find color with right mouse click
    if event == cv.EVENT_RBUTTONDOWN:
        print(x, '', y)
        font = cv.FONT_HERSHEY_SIMPLEX
        # define bgr
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        
        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (255,0,0), 2)
        cv.imshow('image', img)

# Step-3: Driver function to read and display
if __name__=='__main__':
    # read an image
    img = cv.imread('resources/chef.jpg', 1)
    # display the image
    cv.imshow('image', img)
    # set callback function
    cv.setMouseCallback('image', find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()