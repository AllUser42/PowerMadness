#power madness
import pygame
from pygame.locals import*
import random
import sys
import pygwidgets

#Window settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FRAMES_PER_SECOND = 30

#Colors
RED = (255,0,0)
ORANGE = (255,128,0)
YELLOW = (255,255,0)
GREEN = (0,153,0)
BLUE = (0,0,255)
PURPLE = (127,0,255)                
BLACK = (0,0,0)
WHITE = (255,255,255)


#Initialize world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()


#Load Image
startMenu = pygame.image.load("menuPlaceHolderGame.jpg")
backGroundImage = pygame.image.load("images/background.jpg")



#Levels
START = 'start'
LEVEL_ONE = 'level one'
LEVEL_TWO = 'level two'
LEVEL_THREE = 'level three'

#Buttons
startGame = pygwidgets.TextButton(window, (45, 655), 'start game')

#Images chcange
#cityImage = pygwidgets.ImageCollection(window, (100, 200),\
                                     #{‘image1’:’images/SomeImage.png’, ‘image2’:’images/Image2.png’, ‘image3’:’images/Image3.png’}, ‘image1’)


state = START

#Main loop

while True:
    if state == START:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if startGame.handleEvent(event):
                print('start game')
                state = LEVEL_ONE
            



            
        window.blit(startMenu, (0, 0))
        startGame.draw()
        #cityImage.draw()
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)

    elif state == LEVEL_ONE or state == LEVEL_TWO or state == LEVEL_THREE:
        if state == LEVEL_ONE:
            print('in level one')
            window.blit(backGroundImage,(0,0))
            pygame.display.update()
            clock.tick(FRAMES_PER_SECOND)
        
                
