#power madness
import pygwidgets
import pygame
from pygame.locals import*
import random
import sys
import constants
from colors import *

#---------Start constants---------
fontName = pygame.font.match_font('Arial')
    
POWERGENERATORLIST = []
#---------End Constants----------
#--------Windows settings------------
WIDTH = 1280
LENGTH = 720
FRAME_RATE = 30

#----------End Windows settings-------

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


def myFunction(theNickname):
    if theNickname is None:
        print('In myFunction, a button was clicked')
    else:
        print('In myFunction, the button named', theNickname, 'was clicked')


def texts(text, size, color, x, y):
    font = pygame.font.Font(fontName,size)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = (x,y)
    window.blit(textSurface,textRect)
    


window = pygame.display.set_mode([WIDTH,LENGTH])
window.fill(BLACK)
displayTextB = pygwidgets.DisplayText(window, (20, 400), 'Here is some display text', \
                                    fontSize=24, textColor=YELLOW, backgroundColor=BLACK)

inputTextA = pygwidgets.InputText(window, (20, 100), 'Default input text',\
                                    textColor=WHITE, backgroundColor=BLACK,
                                    fontSize=24, width=250)


inputTextB = pygwidgets.InputText(window, (20, 200), initialFocus=True,\
                                    textColor=(0, 0, 255),
                                    fontSize=28)






box1rect = pygame.Rect(10,10,250,100) #button placement

box1rect = pygame.Rect(10,10,250,100) #button placement
box_1 = pygame.draw.rect(window, YELLOW, box1rect) # these are the boxes i have placed
box_2 = pygame.draw.rect(window, YELLOW, [280,10,250,100])
box_3 = pygame.draw.rect(window, YELLOW, [550,10,250,100]) 
box_4 = pygame.draw.rect(window, YELLOW, [10,600,250,100]) 
box_5 = pygame.draw.rect(window, YELLOW, [280,600,250,100])
box_6 = pygame.draw.rect(window, YELLOW, [550,600,250,100])
box_7 = pygame.draw.rect(window, YELLOW, [800,130,400,450]) #place holder for city
box_1_centerx = box_1.centerx
box_1_centery = box_1.centery #place holder for city


texts('PLACE HOLDER', 30, WHITE, box_1.centerx, box_1.centery)

restartButton = pygwidgets.CustomButton(window, (box_1.centerx, box_1.centery), \
                                    'images/RestartButtonUp.png',
                                    down='images/RestartButtonDown.png',
                                    over='images/RestartButtonOver.png',
                                    disabled='images/RestartButtonDisabled.png',
                                    soundOnClick='sounds/blip.wav',
                                    nickname='RestartButton',
                                    callBack=myFunction)











clock = pygame.time.Clock()

pygame.display.update()
clock.tick(FRAME_RATE)




counter = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if box1rect.collidepoint(event.pos): # invisible button
                
                print('clicked in box 1')

        if restartButton.handleEvent(event):  # clicked
            counter = 0
            print('Content of first input text is:', inputTextA.getValue())
            print('Content of second input text is:', inputTextB.getValue())
    
  




    
    counter = counter + 1
    restartButton.draw()
    pygame.display.update()
    clock.tick(FRAME_RATE)
    







