import pygame
from colors import *
import pygwidgets
from functions import *
from pygame.locals import*
#--------- window settings--------
WIDTH = 1280
LENGTH = 720
FRAME_RATE = 30
#---------end window settings-----

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




restartButton = pygwidgets.CustomButton(window, (10, 10), \
                                    'images/RestartButtonUp.png',
                                    down='images/RestartButtonDown.png',
                                    over='images/RestartButtonOver.png',
                                    disabled='images/RestartButtonDisabled.png',
                                    soundOnClick='sounds/blip.wav',
                                    nickname='RestartButton',
                                    callBack=myFunction)



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
box_1_centery = box_1.centery


restartButton.draw()
pygame.display.update()
clock.tick(FRAME_RATE)
