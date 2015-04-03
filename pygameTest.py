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
    def draw(self, screen):
        pygame.draw.polygon(screen, (0,0,0), [(self.xPos-self.width, self.yPos-self.height), (self.xPos-self.width, self.yPos+self.height), (self.xPos+self.width, self.yPos+self.height), (self.xPos+self.width, self.yPos-self.height)])

def drawGoal(xPos,yPos, height, width):
    pygame.draw.polygon(screen, (200,200,0), [(xPos-width, yPos-height), (xPos-width, yPos+height), (xPos+width, yPos+height), (xPos+width, yPos-height)])

def updateGoal(goal, loc, gridWidth, gridHeight, gridCenterX, gridCenterY):
    print("hey")
    (x,y) = loc
    start = 0
    xLoc = 0
    count = 0
    while 1:
        if(x >= start and x <= start+gridWidth):
            break
        else:
            xLoc += 1
            start += gridWidth
            count+=1
        if count > 100 :
            break
    start = 0
    yLoc = 0
    count = 0
    while 1:
        if(y >= start and y <= start+gridHeight):
            break
        else:
            yLoc += 1
            start += gridHeight
            count+=1
        if count > 100 :
            break
    print(xLoc, yLoc)
    return (xLoc*gridWidth+gridCenterX, yLoc*gridHeight+gridCenterY)

clock = pygame.time.Clock()
pygame.init()
size = width, height = 144*7, 90*7
screen = pygame.display.set_mode(size)
xPos, yPos = width/2, height/2
xPosTry = xPos
yPosTry = yPos
vel = 10
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
goal = (gridCenterX,gridCenterY)
radius = int((.5*min(gridCenterX, gridCenterY)))
clickCount = 0
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
        angle -= 1
    if keys[pygame.K_RIGHT]:# or keys[pygame.K_D]:
        angle += 1
    #angle += int(rng.randint(-5,5))

    if pygame.mouse.get_pressed()[0] and clickCount == 0:
        pos = pygame.mouse.get_pos()
        goal = updateGoal(goal, pos, gridWidth, gridHeight, gridCenterX, gridCenterY)
        clickCount = 20

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

    #if(xcol == 0):
    xPos += np.cos(angle*np.pi/180)
    #if(ycol == 0):    
    yPos += np.sin(angle*np.pi/180)

    if(xPos+radius > width):
        xPos = width-radius
    if(yPos+radius > height):
        yPos = height-radius
    if(xPos-radius < 0):
        xPos = radius
    if(yPos-radius < 0):
        yPos = radius

    screen.fill((200,200,200))
    drawGoal(goal[0], goal[1], gridCenterY, gridCenterX)
    pygame.draw.circle(screen, (0,0,255), (int(xPos), int(yPos)), radius, 0)
    for x in obstacles:
        x.draw(screen)
    pygame.draw.line(screen, (255,0,0), (int(xPos),int(yPos)), (int(xPos + np.cos(angle*np.pi/180) * radius), int(yPos + np.sin(angle*np.pi/180)*radius)), 2)
    pygame.display.flip()
    clock.tick(60)

    if(clickCount > 0):
        clickCount -= 1
