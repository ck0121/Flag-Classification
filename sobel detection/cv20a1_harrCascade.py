import cv2 as cv

haarcPath =''
cascadeFace = cv.CascadeClassifier(haarcPath + 'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)
while True:
  ret, img = cap.read()
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  found = cascadeFace.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)
  for (x,y,w,h) in found:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
  cv.imshow('Haar Cascade Object Detection using OpenCV', img)
  key = cv.waitKey(20)
  if key==27: # user pressed the Escape key
    break

cap.release()
cv.destroyAllWindows()
