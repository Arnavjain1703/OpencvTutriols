import cv2
import numpy as np

img = cv2.imread("images/myimage.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)

cv2.waitKey(0)

