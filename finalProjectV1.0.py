#power madness
import pygwidgets
import pygame
from pygame.locals import*
import random
import sys
#---------Start constants---------
fontName = pygame.font.match_font('Arial')
    
POWERGENERATORLIST = []
#---------End Constants----------
#--------Windows settings------------
WIDTH = 1280
LENGTH = 720
FRAME_RATE = 30

#----------End Windows settings-------
#-----------game functions--------
malfunction = random.randrange(1,11)
POWER_OUTPUT = 0.00
inventory = []
citySize = 0
BACKROUND_COLOR = (0,0,0)
SECOND_COLOR = (255,255,0)
WHITE = (0,0,255)

#---------end game function----------
#------------pywigets start------

#-----------pywigets ends------------
#-----------pygame--------------

#----------end pygame------------

def buyNewGenerator():
    #TODO
    #generator output
    #generator counter
    #generator
    
    pass

def city():
    #TODO
    #power comsumtion
    
    #output cash
    
    pass

def powerCheckOfCity():
    #TODO
    #check to see if power is greater than 25%
    pass


def randomMalfunction():
    pass

def texts(text, size, color, x, y):
    font = pygame.font.Font(fontName,size)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = (x,y)
    window.blit(textSurface,textRect)
    


window = pygame.display.set_mode([WIDTH,LENGTH])
window.fill(BACKROUND_COLOR)

box1rect = pygame.Rect(10,10,250,100) #button placement
box_1 = pygame.draw.rect(window, SECOND_COLOR, box1rect) # these are the boxes i have placed
box_2 = pygame.draw.rect(window, SECOND_COLOR, [280,10,250,100])
box_3 = pygame.draw.rect(window, SECOND_COLOR, [550,10,250,100]) 
box_4 = pygame.draw.rect(window, SECOND_COLOR, [10,600,250,100]) 
box_5 = pygame.draw.rect(window, SECOND_COLOR, [280,600,250,100])
box_6 = pygame.draw.rect(window, SECOND_COLOR, [550,600,250,100])
box_7 = pygame.draw.rect(window, SECOND_COLOR, [800,130,400,450]) #place holder for city
box_1_centerx = box_1.centerx
box_1_centery = box_1.centery
texts('PLACE HOLDER', 30, WHITE, box_1.centerx, box_1.centery)


clock = pygame.time.Clock()

pygame.display.update()
clock.tick(FRAME_RATE)






while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if box1rect.collidepoint(event.pos): # invisible button
                
                print('clicked in box 1')

    
   







