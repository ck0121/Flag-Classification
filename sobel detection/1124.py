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
  button_1 = button_create('Load', (150, 450, 100, 50), C_green, C_b_green, load_img)
  button_2 = button_create('Contours', (300, 450, 100, 50), C_green, C_b_green, Bounding)
  button_3 = button_create('Bounding', (450, 450, 100, 50), C_green, C_b_green, getContours)
  button_4 = button_create('Gen XML', (600, 450, 100, 50), C_green, C_b_green, gen_xml)

  quit = True
  while quit:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit = False
      button_check(button_1, event)
      button_check(button_2, event)
      button_check(button_3, event)
      button_check(button_4, event)

    gameDisplay.fill(C_white)

    button_draw(gameDisplay, button_1)
    button_draw(gameDisplay, button_2)
    button_draw(gameDisplay, button_3)
    button_draw(gameDisplay, button_4)
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


def button_create(text, rect, ic, ac, action=None):

    font = pygame.font.Font(None, 20)

    button_rect = pygame.Rect(rect)

    text_button = font.render(text, True, C_black)
    text_button_rect = text_button.get_rect(center=button_rect.center)

    return [text_button, text_button_rect, button_rect, ic, ac, action, False]

def button_check(info, event):

    text, text_rect, rect, ic, ac, action, hover = info

    if event.type ==pygame.MOUSEBUTTONDOWN:
        # hover = True/False
        info[-1] = rect.collidepoint(event.pos)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and action:
            action()

def button_draw(gameDisplay, info):

    text, text_rect, rect, ic, ac, action, hover = info

    if hover:
        color = ac
    else:
        color = ic

    pygame.draw.rect(gameDisplay, color, rect)
    gameDisplay.blit(text, text_rect)




# def button(msg, x, y, w, h, ic, ac, action=None):
#   mouse = pygame.mouse.get_pos()
#   click = pygame.mouse.get_pressed()
#   if x + w > mouse[0] > x and y + h > mouse[1] > y:
#     pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
#     if click[0] ==1  and action != None:
#       action()
#   else:
#     pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
#   smallText = pygame.font.SysFont('comicsansms', 20)
#   textSurf, textRect = text_objects(msg, smallText)
#   textRect.center = (x + w / 2, y + h / 2)
#   gameDisplay.blit(textSurf, textRect)






def getContours():
  global imgOutPyg
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

def Bounding():
  global imgOutPyg2
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
  print(xmin, ymin, xmax, ymax)
  cv.rectangle(imgContour, (xmin, ymin),(xmax, ymax),(255,0,0),2)
  cv.imwrite('Resources/002_new.png', imgContour)






def gen_xml():
  GenerateXML(r'Resources\Xml12345.xml')


#--------------------------------------------------------------------

pygame.init()
load_img()
game_loop()
pygame.quit()

