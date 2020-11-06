import cv2
import numpy as np

path = 'Resources/Ahw0238.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
_, Thresh = cv2.threshold(imgBlur,20,255,cv2.THRESH_BINARY)
imgDilated = cv2.dilate(Thresh,None,iterations = 3)
Contours, _ = cv2.findContours(imgDilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for contour in Contours:
    (x,y,w,h) = cv2.boundingRect(contour)

    if cv2.contourArea(contour) < 700:
        continue
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)



cv2.drawContours(img, Contours, -1, (0,255,0), 3)

imgCanny = cv2.Canny(imgBlur,50,50)

cv2.imshow("Image",img)
cv2.waitKey(0)