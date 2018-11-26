#power madness
import pygwidgets
import pygame
from pygame.locals import*
import random
import sys
from constants import *
from colors import *
import window
from functions import *
#---------Start constants---------

    
POWERGENERATORLIST = []
#---------End Constants----------



#window settings here



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if box1rect.collidepoint(event.pos): # invisible button
                
                print('clicked in box 1')
            

        #if restartButton.handleEvent(event):  # clicked
            
            print('Content of first input text is:', inputTextA.getValue())
            print('Content of second input text is:', inputTextB.getValue())
    
  




    
    
    
    







