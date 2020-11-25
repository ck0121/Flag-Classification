import cv2
import pygame
import time

pygame.init()

path = 'Resources/Ahw0247.png'
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur,50,50)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)

screen_width = 800
screen_height = 600

#image pos
majorX = 200
majorY = 100

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bounding Box')
icon = pygame.image.load('box.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
majorImg = pygame.image.load('Ahw0247.png')

def getContours():
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    xmin, ymin, xmax, ymax = 500, 500, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area<100:
            continue
        else:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 1)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            #print (x,y,w,h)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            print(x,y,x+w,y+h)

            if xmin > x:
                xmin = x
            if ymin > y:
                ymin = y
            if xmax < x+w:
                xmax = x+w
            if ymax < y+h:
                ymax = y+h
    print(xmin, ymin, xmax, ymax)

    cv2.rectangle(imgContour, (xmin, ymin),(xmax, ymax),(255,0,0),2)
    cv2.imwrite('/Resources/001_new.png', img)


def major(X,Y):
    screen.blit(majorImg, (X, Y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_diaplay(text):
    largeText = pygame.font.SysFont('comicsansms', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screen_width / 2), (screen_height / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    ##                if action == "play":
    ##                    action()
    ##                if action == "quit":
    ##                    pygame.quit()
    ##                    quit()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.SysFont('comicsansms', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('Bounding Box', largeText)
        TextRect.center = ((screen_width / 2), (screen_height / 2))
        screen.blit(TextSurf, TextRect)
        button("GO", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = 200
    y = 100

    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)

        screen.blit(majorImg, (x,y))
        button("Load", 130, 450, 100, 50, green, bright_green, getContours)
        button("Make", 270, 450, 100, 50, red, bright_red, quitgame)
        button("Mix", 410, 450, 100, 50, green, bright_green, game_loop)
        button("XML", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)

    pygame.display.update()
    clock.tick(60)
def game_load():
    path = 'Resources/Ahw0247.png'
    img = cv2.imread(path)
    screen.blit()





def game_Contour():
    x = 200
    y = 100

    imgContour = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContours(imgCanny)
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)

        screen.blit(imgContour, (x,y))
        button("Load", 130, 450, 100, 50, green, bright_green, game_load)
        button("Make", 270, 450, 100, 50, red, bright_red, game_Contour)
        button("Mix", 410, 450, 100, 50, green, bright_green, game_loop)
        button("XML", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)


# crash()

game_intro()
game_loop()

getContours(imgCanny)
game_Contour()
pygame.quit()
quit()