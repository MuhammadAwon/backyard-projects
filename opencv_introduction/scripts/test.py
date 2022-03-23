import cv2
import numpy as np

img = cv2.imread('resources/card.jpg')

width, height = 250, 350
pts1 = np.float32([[51,101], [130,88], [71,220], [161,200]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
print(pts1)
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output =cv2.warpPerspective(img, matrix, (width,height))


for x in range(0,4):
    cv2.circle(img, center=(int(pts1[x][0]), int(pts1[x][1])), radius=5, color=(0,255,0), thickness=cv2.FILLED)


cv2.imshow('original image', img)
cv2.imshow('output image', output)
cv2.waitKey(0)