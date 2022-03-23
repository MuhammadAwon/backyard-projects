import cv2 as cv
import numpy as np

# Create a function to stack multiple images of different sizes and tones
def stack_images(img1, img2, axis=None):
    color_img = cv.imread(img1)
    gray_img = cv.imread(img2, 0) # load image in grayscale mode
    
    # Resize images
    color_img = cv.resize(color_img, (400,250))
    gray_img = cv.resize(gray_img, (400,250))

    # Convert grayscale image to 3-channel image, so that they can be stacked together    
    gray_img = cv.cvtColor(gray_img, cv.COLOR_GRAY2BGR)
    
    # Conditional statement for vertical and horizontal stacking
    if axis == 0:
        both_imgs = np.concatenate((color_img, gray_img), axis=axis) # 0 : vertical stack
        cv.imshow('Vertical stack', both_imgs)
    else:
        both_imgs = np.concatenate((color_img, gray_img), axis=axis) # 1 : horzontal stack
        cv.imshow('Horizontal stack', both_imgs)


    return both_imgs


images = stack_images(img1='resources/chef.jpg', img2='resources/chef.jpg', axis=1)

# Initialize wait key 
cv.waitKey(0)
cv.destroyAllWindows()