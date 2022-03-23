# Save an image
import cv2 as cv
from cv2 import imwrite

img = cv.imread('resources/space.jpg')
img = cv.resize(img, (400, 400))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(tresh, binary) = cv.threshold(gray, 127, 225, cv.THRESH_BINARY)

imwrite('resources/gray_space.png', gray)
imwrite('resources/b&w_space.png', binary)

cv.waitKey(0)
cv.destroyAllWindows()