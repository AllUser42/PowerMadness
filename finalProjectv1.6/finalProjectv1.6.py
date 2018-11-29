#power madness
import pygame
from pygame.locals import*
import random
import sys
import pygwidgets


#-------------------Pywidgets----------------------------


#-------------------End Pywidgets------------------------


#------Window-------
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FRAMES_PER_SECOND = 30
#-----End Window----

#-----Game Constants-------
numberOfGenerators1 = 0

#-----End Game Constants---

#-------Colors---------
RED = (255,0,0)
ORANGE = (255,128,0)
YELLOW = (255,255,0)
GREEN = (0,153,0)
BLUE = (0,0,255)
PURPLE = (127,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
#-----End Colors-----


#-----Initialize the world--------
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
#-----End Initialize the world----

#--------loading Images-----------
backGroundImage = pygame.image.load("images/background.jpg")

#-------End Loading Images--------

#----------Counters---------------
generatorCounter1 = 0
brokenGeneratorCounter = 0

#---------End Counters------------


#----------pygwidgets-------------
buyGenerator1 = pygwidgets.TextButton(window, (45, 655), 'Buy a generator 1')
buyGenerator2 = pygwidgets.TextButton(window, (250, 655), 'Buy a generator 2')
buyGenerator3 = pygwidgets.TextButton(window, (460, 655), 'Buy a generator 3')



#--------End pygwidgets-----------
numberOfGen1Display = pygwidgets.DisplayText(window,(100,45),'0',textColor = WHITE,fontSize = 50)


#-----------Game loop------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if buyGenerator1.handleEvent(event):
            print("Gen button clicked # is" , numberOfGenerators1)
            numberOfGenerators1 = numberOfGenerators1 + 1
            numberOfGen1Display.setValue(numberOfGenerators1)

        if buyGenerator2.handleEvent(event):
            print("Gen2 button clicked")

        if buyGenerator3.handleEvent(event):
            print("Gen3 button clicked")
            
            
                

    window.blit(backGroundImage, (0, 0))
    buyGenerator1.draw()
    buyGenerator2.draw()
    buyGenerator3.draw()
    numberOfGen1Display.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
