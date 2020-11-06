import cv2
import numpy as np

path = "Resources/Ahw0247.png"
img = cv2.imread(path)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)


cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.waitKey(0)