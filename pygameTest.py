import pygame
import random as rng
import numpy as np

pygame.init()
size = width, height = 512, 512
screen = pygame.display.set_mode(size)
xPos, yPos = width/2, height/2
vel = 10
angle = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:# or keys[pygame.K_W]:
        yPos -= 1
    if keys[pygame.K_DOWN]:# or keys[pygame.K_S]:
        yPos += 1
    if keys[pygame.K_LEFT]:# or keys[pygame.K_A]:
        angle -= 5
    if keys[pygame.K_RIGHT]:# or keys[pygame.K_D]:
        angle += 5
    #angle += int(rng.randint(-1,1))

    xPos += np.cos(angle*np.pi/180)
    yPos += np.sin(angle*np.pi/180)

    if(xPos > width):
        xPos = width
    if(yPos > height):
        yPos = height
    if(xPos < 0):
        xPos = 0
    if(yPos < 0):
        yPos = 0

    screen.fill((200,200,200))
    pygame.draw.circle(screen, (0,0,255), (int(xPos), int(yPos)), 20, 0)
    pygame.display.flip()
