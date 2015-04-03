import pygame
import random as rng
import numpy as np
import sys
import grid
import math

class Obstacle:
    #let height/width be the distance from the center
    def __init__(self, x, y, height, width):
        self.xPos = x
        self.yPos = y
        self.height = height
        self.width = width
    '''def collision(self, x, y, r):
        xcol, ycol = 0, 0
        if(x+r > self.xPos - self.width and x-r < self.xPos + self.width and y-r < self.yPos + self.height and y+r > self.yPos - self.height):
            xcol = 1
            ycol = 1
            print("right side of circle")
        ''''''if(x-r < self.xPos + self.width and x-r > self.xPos - self.width and y-r < self.yPos + self.height and y+r > self.yPos - self.height):
            xcol = 1
            print("left side of circle")
        if(x+r > self.xPos - self.width and x-r < self.xPos + self.width and y+r > self.yPos - self.height and y+r < self.yPos + self.height):
            ycol = 1
            print("bottom of circle")
        if(x+r > self.xPos - self.width and x-r < self.xPos + self.width and y-r < self.yPos + self.height and y-r > self.yPos -self.height):
            ycol = 1
            print("top of circle")
        if(xcol == 1 or ycol == 1):
            xcol, ycol = 0, 0
            if(not(x+r > self.xPos - self.width and x+r < self.xPos + self.width and y-r < self.yPos + self.height and y+r > self.yPos - self.height)):
                xcol = 1
                print("right side of circle CHECKER")
            if(not(x-r < self.xPos + self.width and x-r > self.xPos - self.width and y-r < self.yPos + self.height and y+r > self.yPos - self.height)):
                xcol = 1
                print("left side of circle CHECKER")
            if(not(x+r > self.xPos - self.width and x-r < self.xPos + self.width and y+r > self.yPos - self.height and y+r < self.yPos + self.height)):
                ycol = 1
                print("bottom of circle CHECKER")
            if(not(x+r > self.xPos - self.width and x-r < self.xPos + self.width and y-r < self.yPos + self.height and y-r > self.yPos -self.height)):
                ycol = 1
                print("top of circle CHECKER")''''''
        return xcol, ycol'''
    def draw(self, screen):
        pygame.draw.polygon(screen, (0,0,0), [(self.xPos-self.width, self.yPos-self.height), (self.xPos-self.width, self.yPos+self.height), (self.xPos+self.width, self.yPos+self.height), (self.xPos+self.width, self.yPos-self.height)])



pygame.init()
size = width, height = 512, 512
screen = pygame.display.set_mode(size)
xPos, yPos = width/2, height/2
xPosTry = xPos
yPosTry = yPos
vel = 1
angle = 0
g = grid.Grid()
g.readFile("world.txt")
obstacles = []
#get number of cells in each dimension
xGrid, yGrid = len(g.world[0]), len(g.world) 
#get the size of each grid cells
gridHeight = height/yGrid
gridWidth = width/xGrid
gridCenterY = gridHeight/2.0
gridCenterX = gridWidth/2.0
radius = 20
for i in range(len(g.world)):
    for j in range(len(g.world[i])):
        if(g.world[i][j] == "x"):
            temp = Obstacle((j)*gridWidth+gridCenterX, (i)*gridHeight+gridCenterY, gridCenterY, gridCenterX)
            obstacles.append(temp)
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
        angle -= .1
    if keys[pygame.K_RIGHT]:# or keys[pygame.K_D]:
        angle += .1
    #angle += int(rng.randint(-5,5))


    xPosTry = xPos + np.cos(angle*np.pi/180)
    yPosTry = yPos + np.sin(angle*np.pi/180)
    offset = math.sqrt(math.pow(radius,2)/2)
    #xcol, ycol = 0,0
    for x in obstacles:
        if((abs(xPos + radius - (x.xPos - x.width)) < 3) and ((x.yPos - x.height - offset - 3) < yPos < (x.yPos + x.height + offset + 3))):
            xPos = x.xPos - x.width - radius - 3
        if((abs(xPos - radius - (x.xPos + x.width)) < 3) and ((x.yPos - x.height - offset - 3) < yPos < (x.yPos + x.height + offset + 3))):
            xPos = x.xPos + x.width + radius + 3
        if((abs(yPos - radius - (x.yPos + x.height)) < 3) and ((x.xPos - x.width - offset - 3) < xPos < (x.xPos + x.width + offset + 3))):
            yPos = x.yPos + x.height + radius + 3
        if((abs(yPos + radius - (x.yPos - x.height)) < 3) and ((x.xPos - x.width - offset - 3) < xPos < (x.xPos + x.width + offset + 3))):
            yPos = x.yPos - x.height - radius - 3

        '''xcol, ycol = x.collision(xPosTry, yPosTry, radius)
        if(xcol == 1 or ycol == 1):
            break'''
    #if(xcol == 0):
    xPos += .03*np.cos(angle*np.pi/180)
    #if(ycol == 0):    
    yPos += .03*np.sin(angle*np.pi/180)

    if(xPos+radius > width):
        xPos = width-radius
    if(yPos+radius > height):
        yPos = height-radius
    if(xPos-radius < 0):
        xPos = radius
    if(yPos-radius < 0):
        yPos = radius

    screen.fill((200,200,200))
    pygame.draw.circle(screen, (0,0,255), (int(xPos), int(yPos)), radius, 0)
    for x in obstacles:
        x.draw(screen)
    pygame.display.flip()
