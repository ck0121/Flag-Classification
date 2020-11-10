import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Bounding Box")
icon = pygame.image.load('box.png')
pygame.display.set_icon(icon)

majorImg = pygame.image.load('Ahw0247.png')
majorX = 200
majorY = 100

def major(X,Y):
    screen.blit(majorImg, (X, Y))

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

        # keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                print("right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keystoke has been released")



    screen.fill((255,255,255))
    major(majorX,majorY)
    pygame.display.update()
