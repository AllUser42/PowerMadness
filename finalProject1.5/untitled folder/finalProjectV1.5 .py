#power madness
import pygwidgets
import pygame
from pygame.locals import*
import random
import sys
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
#-----------game functions--------
malfunction = random.randrange(1,11)
POWER_OUTPUT = 0.00
inventory = []
citySize = 0
genarator = [pygame.image.load("generatorSmallClip.jpg"),pygame.image.load("generatorMedClip.jpg"),pygame.image.load("generatorLargeClip.jpg")]
#generatorSmall = pygame.image.load("generatorSmallClip.jpg")
#generatorMed = pygame.image.load("generatorMedClip.jpg")
#generatorLarge = pygame.image.load("generatorLargeClip.jpg")
city1List = [pygame.image.load('city1NoPower.jpg'),pygame.image.load('city1MedPower.jpg'),pygame.image.load('city1MaxPower.jpg')]
city2Lsit = [pygame.image.load('city2NoPower.jpg'),pygame.image.load('city2MedPower.jpg'),pygame.image.load('city2MaxPower.jpg')]
City3List = [pygame.image.load('lasVegasNoPower.jpg'),pygame.image.load('lasVegasMedPower.jpg'),pygame.image.load('lasVegasMaxPower.jpg')]
#city1NoPower = pygame.image.load('city1NoPower.jpg')
#city1MedPower = pygame.image.load('city1MedPower.jpg')
#city1MaxPower = pygame.image.load('city1MaxPower.jpg')
#city2NoPower = pygame.image.load('city2NoPower.jpg')
#city2MedPower = pygame.image.load('city2MedPower.jpg')
#city2MaxPower = pygame.image.load('city2MaxPower.jpg')
#city3NoPower = pygame.image.load('lasVegasNoPower.jpg')
#city3MedPower = pygame.image.load('lasVegasMedPower.jpg')
#city3MaxPower = pygame.image.load('lasVegasMaxPower.jpg')
#---------end game function----------
#-------------load pic---------------
small = 0
med = 0
large = 0
counter = 0

def buyNewGenerator():
    #TODO
    #generator output
    #generator counter
    #generator
    
    pass

def city():
    if counter == 0:
        window.blit(city[0](309,402))
        
    
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
    textRect = (x,y)
    window.blit(textSurface,textRect)

def boxes(color, cords1, cords2, size1, sizes2):
    pygame.draw.rect(window, color, [cords1,cords2,size1,sizes2])
    


window = pygame.display.set_mode([WIDTH,LENGTH])
#window.fill(BLACK)
displayTextB = pygwidgets.DisplayText(window, (20, 400), 'Here is some display text', \
                                    fontSize=24, textColor=YELLOW, backgroundColor=BLACK)

inputTextA = pygwidgets.InputText(window, (20, 100), 'Default input text',\
                                    textColor=WHITE, backgroundColor=BLACK,
                                    fontSize=24, width=250)


inputTextB = pygwidgets.InputText(window, (20, 200), initialFocus=True,\
                                    textColor=(0, 0, 255),
                                    fontSize=28)





box1rect = pygame.Rect(550,600,250,100)
box1rect = pygame.Rect(550,600,250,100)
box1rect = pygame.Rect(550,600,250,100)
box1rect = pygame.Rect(550,600,250,100)




#button placement
##box_1 = pygame.draw.rect(window, YELLOW, box1rect) # these are the boxes i have placed

##box_3 = pygame.draw.rect(window, YELLOW, [550,10,250,100]) 
##box_4 = pygame.draw.rect(window, YELLOW, [10,600,250,100]) 
##box_5 = pygame.draw.rect(window, YELLOW, [280,600,250,100])
##box_6 = pygame.draw.rect(window, YELLOW, [550,600,250,100])
##box_7 = pygame.draw.rect(window, YELLOW, [800,130,400,450]) #place holder for city
##box_1_centerx = box_1.centerx
##box_1_centery = box_1.centery
##
#texts('button', 30, WHITE, 100, 100)


box1rect = pygame.Rect(50,640,100,50)
box2rect = pygame.Rect(25,525,40,40)
box3rect = pygame.Rect(75,525,40,40)
box4rect = pygame.Rect(125,525,40,40)



restartButton = pygwidgets.CustomButton(window, (1000,650), \
                                    'images/RestartButtonUp.png',
                                    down='images/RestartButtonDown.png',
                                    over='images/RestartButtonOver.png',
                                    disabled='images/RestartButtonDisabled.png',
                                    soundOnClick='sounds/blip.wav',
                                    nickname='RestartButton',
                                    callBack=myFunction)


backgroundImage= pygame.image.load("background.jpg")


clock = pygame.time.Clock()

pygame.display.update()
clock.tick(FRAME_RATE)

box1MenuActive = False
counter = 0
box2rect = pygame.Rect(0,0,0,0)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if box1rect.collidepoint(event.pos):# invisible button
                city()
                
                window.blit(city1NoPower, (150, 250))
                
            
                          
                


                print('clicked in box 1')

        if restartButton.handleEvent(event):  # clicked
            counter = 0
            
           #print('Content of first input text is:', inputTextA.getValue())
           # print('Content of second input text is:', inputTextB.getValue())
           
    
  



    
    #window.blit(generator, (150, 250)) 
    counter = counter + 1
    
    window.blit(backgroundImage, (0, 0))
    city()
    restartButton.draw()
    #texts('button', 60, WHITE, 100,500)
    box_1 = pygame.draw.rect(window, YELLOW, [50,640,100,50])
    box_2 = pygame.draw.rect(window, YELLOW, [260,640,100,50])
    box_3 = pygame.draw.rect(window, YELLOW, [470,640,100,50])
    box_4 = pygame.draw.rect(window, YELLOW, [680,640,100,50])

##    box2 = boxes(BLACK,0,0,0,0)
##    box3 = boxes(BLACK,0,0,0,0)
##    box4 = boxes(BLACK,0,0,0,0)
##    box5 = boxes(BLACK,0,0,0,0)




    if box1MenuActive == True:
        box2 = boxes(WHITE,25,525,200,100)
        box3 = boxes(BLUE,25,525,40,40)
        box4 = boxes(BLUE,75,525,40,40)
        box5 = boxes(BLUE,125,525,40,40)
    
    pygame.display.update()
    #window.blit(backgroundImage, (0, 0))
    clock.tick(FRAME_RATE)    







