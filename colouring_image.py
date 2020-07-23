import cv2
import numpy as np

img = cv2.imread("images/myimage.jpg")
imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image",imGray)
cv2.waitKey(0)

