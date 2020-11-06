import cv2
import numpy as np

img = cv2.imread("Resources/Ahw0247.png")
print(img.shape)

imgResize = cv2.resize(img,(800,600))
print(imgResize.shape)

imgCropped = img[0:150,200:400]

cv2.imshow("Image",img)
cv2.imshow("Resize Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)
