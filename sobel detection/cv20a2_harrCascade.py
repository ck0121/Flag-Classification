import random
import cv2 as cv

imgNames = [3, 4, 5, 6]
imgId = str(random.choice(imgNames))
if len(imgId)<2: imgId = '0' + imgId
imgNam = 'face-g'+ imgId + '.jpg'

imgSrc = cv.imread(imgNam)
imgGray = cv.cvtColor(imgSrc, cv.COLOR_BGR2GRAY)

haarcPath = ''
cascadeFace = cv.CascadeClassifier(haarcPath + 'haarcascade_frontalface_default.xml')

font = cv.FONT_HERSHEY_SIMPLEX

# color and colorIdx
c = [(255,0,0), (255,255,0), (0,255,0), (0,255,255), (0,0,255), (255,0,255)]
ci = 0

tick = 0
while True:
  imgSrc = cv.imread(imgNam)  # reload imgSrc so we can draw on it again
  # no need to re-convert image to gray scale
  minNbhd = 1 + (tick//4 % 15)
  tick += 1
  ci = (ci+1) % len(c)
  found = cascadeFace.detectMultiScale(imgGray, scaleFactor=1.3, minNeighbors=minNbhd)
  for (x,y,w,h) in found:
    cv.rectangle(imgSrc, (x,y), (x+w,y+h), c[ci], 2)
  s = f'img#{imgId}   minNbhd={minNbhd}   faces={len(found)}'
  cv.putText(imgSrc, s, (10, 30), font, 0.7, c[ci], 2, cv.LINE_AA)
  cv.imshow('Haar Cascade Object Detection using OpenCV', imgSrc)
  key = cv.waitKey(50)
  if key==27: # user pressed the Escape key
    break


