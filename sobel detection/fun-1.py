from fun_global import *
from XML_Function import *
import pygame
import cv2 as cv


# 'global' variables shared by different image processing routines
imgPath = None
imgSrc = None       # source image loaded using OpenCV
imgSrcPyg = None    # source image converted to PyGame
imgOut = None       # generated image (from source) using OpenCV routine
imgOutPyg = None    # pygame-version of imgOut (for display only)
imgOutpyg2 = None   # pygame-version of imgOutPyg of box
a = []

# 'global' variables used by this app
scrW = 1240 # display width
scrH = 600 # display height
target_fps = 40 # frames per second
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrW, scrH))
pygame.display.set_caption('Fun 1')




#------------------------------------------------------------------

imgId = 0
imgFilename = ['Ahw0247', 'Ahw0155', 'Chw0003']

def load_img():
  global imgPath, imgSrc, imgSrcPyg, imgOutPyg2,imgId
  imgPath = 'Resources/' + imgFilename[imgId] + '.png'
  imgId = (imgId+1) % len(imgFilename)
  imgSrc = cv.imread(imgPath)
  imgSrcPyg = cvImageToSurface(imgSrc)
  imgOut = None
  imgOutPyg = None
  imgOutPyg2 = None


def game_loop():
  quit = False
  while not quit:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit = True
      elif event.type ==pygame.MOUSEBUTTONDOWN:

        break
    gameDisplay.fill(C_white)
    button('Load', 150, 450, 100, 50, C_green, C_b_green, load_img)
    button('Contours', 300, 450, 100, 50, C_green, C_b_green, Bounding)
    button('Bounding', 450, 450, 100, 50, C_green, C_b_green, getContours)
    button('Gen XML', 600, 450, 100, 50, C_green, C_b_green, gen_xml)
    draw_image(imgSrcPyg, 10, 10)
    draw_image(imgOutPyg2, 420, 10)
    draw_image(imgOutPyg, 830, 10)
    pygame.display.update()
    clock.tick(target_fps)

#--------------------------------------------------------------------

def draw_image(imgPyg, x, y):
  if imgPyg != None:
    gameDisplay.blit(imgPyg, (x, y))

def text_objects(text, font):
  textSurface = font.render(text, True, C_black)
  return textSurface, textSurface.get_rect()

clickProcessed = False
def button(msg, x, y, w, h, ic, ac, action=None):
  global clickProcessed
  mouse = pygame.mouse.get_pos()
  #click = pygame.mouse.get_pressed()

  (sL, sM, sR) = pygame.mouse.get_pressed(num_buttons=3)
  if not clickProcessed and sL:
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
      print('hello')
      clickProcessed = True
  else:
    clickProcessed = False

  # if click:
  #   print('mouse clicked')
  #   if x + w > mouse[0] > x and y + h > mouse[1] > y:
  #     pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
  #     if click[0] ==1  and action != None:
  #       action()
  #     else:
  #       pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
  # smallText = pygame.font.SysFont('comicsansms', 20)
  # textSurf, textRect = text_objects(msg, smallText)
  # textRect.center = (x + w / 2, y + h / 2)
  # gameDisplay.blit(textSurf, textRect)






def getContours():
  global imgOutPyg, a
  imgGray = cv.cvtColor(imgSrc, cv.COLOR_BGR2GRAY)
  imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
  imgCanny = cv.Canny(imgBlur, 50, 50)
  imgOutPyg = cvImageToSurface(imgSrc)
  contours, hierarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
  xmin, ymin, xmax, ymax = 500, 500, 0, 0
  imgContour = None
  for cnt in contours:
    area = cv.contourArea(cnt)
    # print('area', area)
    if area<100:
      continue
    else:
      imgContour = imgSrc.copy()
      cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)
      peri = cv.arcLength(cnt,True)
      # print('peri', peri)
      approx = cv.approxPolyDP(cnt,0.02*peri,True)
      # print('approx', approx)
      # objCor = len(approx)
      x, y, w, h = cv.boundingRect(approx)
      # print (x,y,w,h)
      cv.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
      # print(x,y,x+w,y+h)
      if xmin > x:    xmin = x
      if ymin > y:    ymin = y
      if xmax < x+w:  xmax = x+w
      if ymax < y+h:  ymax = y+h
  print(xmin, ymin, xmax, ymax)
  cv.rectangle(imgSrc, (xmin, ymin),(xmax, ymax),(255,0,0),2)
  cv.imwrite('Resources/002_new.png', imgSrc)
  a = [xmin,ymin,xmax,ymax]
  return a

def Bounding():
  global imgOutPyg2, a
  imgGray = cv.cvtColor(imgSrc, cv.COLOR_BGR2GRAY)
  imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
  imgCanny = cv.Canny(imgBlur, 50, 50)
  imgOutPyg2 = cvImageToSurface(imgCanny)
  contours, hierarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
  xmin, ymin, xmax, ymax = 500, 500, 0, 0
  imgContour = None
  for cnt in contours:
    area = cv.contourArea(cnt)
    # print('area', area)
    if area<100:
      continue
    else:
      imgContour = imgSrc.copy()
      cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)
      peri = cv.arcLength(cnt,True)
      # print('peri', peri)
      approx = cv.approxPolyDP(cnt,0.02*peri,True)
      # print('approx', approx)
      # objCor = len(approx)
      x, y, w, h = cv.boundingRect(approx)
      # print (x,y,w,h)
      cv.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
      # print(x,y,x+w,y+h)
      if xmin > x:    xmin = x
      if ymin > y:    ymin = y
      if xmax < x+w:  xmax = x+w
      if ymax < y+h:  ymax = y+h

  cv.rectangle(imgContour, (xmin, ymin),(xmax, ymax),(255,0,0),2)
  cv.imwrite('Resources/002_new.png', imgContour)
  a = [xmin,ymin,xmax,ymax]

  print('xmin,ymin,xmax,ymax=',a)
  return a

# def GenerateXML(filename):
#     global a
#     a = []
#     # 在内存中创建一个空的文档
#     doc = xml.dom.minidom.Document()
#     # 创建一个根节点Managers对象
#     root = doc.createElement('annotation')
#
#     # 将根节点添加到文档对象中
#     doc.appendChild(root)
#
#     # 根节点Annotation和子节点Folder,Filename,path
#     nodeFolder = doc.createElement("folder")
#     nodeFolder.appendChild(doc.createTextNode("Folder Name"))
#     nodeFilename = doc.createElement("filename")
#     nodeFilename.appendChild(doc.createTextNode("File Name"))
#     nodePath = doc.createElement("path")
#     nodePath.appendChild(doc.createTextNode("Path"))
#
#     # 父节点Size和子节点Width,Height
#     nodeSize = doc.createElement("Size")
#     nodeWidth = doc.createElement("Width")
#     nodeWidth.appendChild(doc.createTextNode('400'))
#     nodeHeight = doc.createElement("Height")
#     nodeHeight.appendChild(doc.createTextNode('300'))
#
#     # 父节点Object和子节点Name(label),Bndbox
#     nodeObject = doc.createElement("object")
#     nodeName = doc.createElement("name")
#     nodeName.appendChild(doc.createTextNode('label'))
#
#     # 父节点Bndbox和子节点Xmin,Ymin,Xmax,Ymax
#     nodeBndbox = doc.createElement("bndbox")
#     nodeXmin = doc.createElement("xmin")
#     nodeXmin.appendChild(doc.createTextNode(str(a[0])))
#     nodeYmin = doc.createElement("ymin")
#     nodeYmin.appendChild(doc.createTextNode(str(a[1])))
#     nodeXmax = doc.createElement("xmax")
#     nodeXmax.appendChild(doc.createTextNode(str(a[2])))
#     nodeYmax = doc.createElement("ymax")
#     nodeYmax.appendChild(doc.createTextNode(str(a[3])))
#
#     # 将子节点添加到父节点下
#     nodeSize.appendChild(nodeWidth)
#     nodeSize.appendChild(nodeHeight)
#
#     nodeObject.appendChild(nodeName)
#     nodeObject.appendChild(nodeBndbox)
#
#     nodeBndbox.appendChild(nodeXmin)
#     nodeBndbox.appendChild(nodeYmin)
#     nodeBndbox.appendChild(nodeXmax)
#     nodeBndbox.appendChild(nodeYmax)
#
#     # 将父节点添加到根节点下
#     root.appendChild(nodeFolder)
#     root.appendChild(nodeFilename)
#     root.appendChild(nodePath)
#     root.appendChild(nodeSize)
#     root.appendChild(nodeObject)
#
#     # 开始写xml文档
#     fp = open(filename, 'w')
#     doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")




def gen_xml():
  global a

  GenerateXML(r'Resources\Xml12345.xml')


#--------------------------------------------------------------------

pygame.init()
load_img()
GenerateXML(r'D:\Blander Flag\Flag-Classification\sobel detection\Resources\Xml12.xml')
game_loop()
pygame.quit()
quit()
