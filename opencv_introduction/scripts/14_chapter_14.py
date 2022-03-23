# How to draw lines and shapes in python
import cv2 as cv
from cv2 import imwrite
import numpy as np

# Draw a canvas
img = np.zeros((600, 600)) # 0: black
img1 = np.ones((600, 600)) # 1: white

# Image size
print(f'The size of our canvas is: {img.shape}')
# print(img)

# Add colors shape to the image
colored_img = np.zeros((600,600, 3), np.uint8) # add color channel

# Complete colored image
colored_img[:] = 255,0,225

# Part of image to be colored
colored_img[150:230, 100:500] = 255,168,10

# Add line
cv.line(colored_img, (100,100), (300,300), (255,255,50), 3) # part of image with line

# Add line to complete image
cv.line(colored_img, (0,0), (colored_img.shape[0], colored_img.shape[1]), (255,0,0), 3)

# Add rectangles
cv.rectangle(colored_img, (50,100), (300,400), (255,255,255), 3) # draw rectangle
cv.rectangle(colored_img, (50,100), (300,400), (255,255,255), cv.FILLED) # fill rectangle

# Add circle
cv.circle(colored_img, (400,300), 50, (255,100,0), 5)
cv.circle(colored_img, (400,300), 50, (255,100,0), cv.FILLED)

# Add text
# cv.putText(colored_img, 'Python ka Chilla on Codanics YouTube Channel', (200,500), cv.FONT_ITALIC, 1, (255,255,0), 1)

# Add text in multiple lines
text = "Python ka Chilla \n on Codanics YouTube Channel"
position = (100, 30)
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 0.75
color = (100, 100, 100)
thickness = 2
line_type = cv.LINE_AA

text_size, _ = cv.getTextSize(text, font, font_scale, thickness)
line_height = text_size[1] + 5
x, y0 = position
for i, line in enumerate(text.split("\n")):
    y = y0 + i * line_height
    cv.putText(colored_img, line, (x, y), font, font_scale, color, thickness, line_type)




# cv.imshow('Black image', img)
# cv.imshow('White image', img1)
cv.imshow('Colored Image', colored_img)
# imwrite('resources/multitext_image.png', colored_img) ## save image
cv.waitKey(0)
cv.destroyAllWindows()