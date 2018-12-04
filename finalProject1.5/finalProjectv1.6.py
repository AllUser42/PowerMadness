#power madness
import pygame
from pygame.locals import*
import random
import sys
import pygwidgets


#------Window-------
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FRAMES_PER_SECOND = 30
#-----End Window----

#-----Game Constants-------
##numberOfGenerators1 = 0
##numberOfGenerators2 = 0
##numberOfGenerators3 = 0
##
##cityPowerDemand1 = 50
##cityPowerDemand2 = 100
##cityPowerDemand3 = 150



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
generatorCounter2 = 0
generatorCounter3 = 0

brokenGeneratorCounter = 0

#---------End Counters------------


#----------pygwidgets buttons-------------
##def generatorButtons():
##    buyGenerator1 = pygwidgets.TextButton(window, (45, 655), 'Buy a generator 1')
##    buyGenerator2 = pygwidgets.TextButton(window, (250, 655), 'Buy a generator 2')
##    buyGenerator3 = pygwidgets.TextButton(window, (460, 655), 'Buy a generator 3')




#----------pywidgets display text----------------

##def displayGameData():
##    numberOfGen1Display = pygwidgets.DisplayText(window,(400 , 45),'0',textColor = WHITE,fontSize = 50)
##    numberOfGen2Display = pygwidgets.DisplayText(window,(700 , 45),'0',textColor = WHITE,fontSize = 50)
##    numberOfGen3Display = pygwidgets.DisplayText(window,(800 , 45),'0',textColor = WHITE,fontSize = 50)
##    cityPowerDemand = pygwidgets.DisplayText(window,(600 , 45), '1', textColor = WHITE , fontSize = 50)

def wonGameScreen():
    wonGameScreen = pygame.image.load("images/winScreen.jpg")
    
    nextLevel = pygwidgets.TextButton(window, (45, 655), 'Continue to next level')
    quitGame = pygwidgets.TextButton(window, (45, 555), 'quit game')
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if quitGame.handleEvent(event):
                pygame.quit()
                quit()

            if nextLevel.handleEvent(event):
                print('Go to next level')
                gameLevel2()

        window.blit(wonGameScreen, (0, 0))
        nextLevel.draw()
        quitGame.draw()
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)





def startMenu():
    WHITE = (255,255,255)
    startMenu = pygame.image.load("menuPlaceHolderGame.jpg")
    
    start = pygwidgets.TextButton(window, (45, 655), 'start game')
    quitGame = pygwidgets.TextButton(window, (45, 555), 'quit game')
    
    #starMenuButton = pygwidgets.DisplayText(window (400,50),'Start', textColor = WHITE,fontSize=50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if start.handleEvent(event):
                print("Start")
                gameLevel1()

            if quitGame.handleEvent(event):
                print("quit")
                pygame.quit()
                quit()

        window.blit(startMenu, (0, 0))
        start.draw()
        quitGame.draw()

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)

#City 1 power 
def cityImageLevelOneCityOne():
    city1no = pygame.image.load('city1NoPower.jpg')
    

def cityImageLevelTwoCityOne():
    city1Med = pygame.image.load('city1MedPower.jpg')
    window.blit(city1Med,(585,174))

def cityImageLevelThreeCityOne():
    city1Max = pygame.image.load('city1MaxPower.jpg')
    window.blit(city1Max,(585,174))

#City 2 power
    
def cityImageLevelOneCityTwo():
    city2no = pygame.image.load('city2NoPower.jpg')
    window.blit(city2no,(585,174))
def cityImageLevelTwoCityTwo():
    city2Med = pygame.image.load('city2MedPower.jpg')
    window.blit(city2Med,(585,174))
def cityImageLevelThreeCityTwo():
    city2Max = pygame.image.load('city2MaxPower.jpg')
    window.blit(city2Max,(585,174))

#city 3 power
def cityImageLevelOneCityTwo():
    city3no =
    window.blit(city3,(585,174))
def cityImageLevelOneCityTwo():
    city3Med =
    window.blit(city3,(585,174))
def cityImageLevelOneCityTwo():
    city3Max = 
    window.blit(city3,(585,174))



def gameLevel1():
    #Buttons to buy generators
    buyGenerator1 = pygwidgets.TextButton(window, (45, 655), 'Buy a generator 1')
    buyGenerator2 = pygwidgets.TextButton(window, (250, 655), 'Buy a generator 2')
    buyGenerator3 = pygwidgets.TextButton(window, (460, 655), 'Buy a generator 3')

    #Display game data
    numberOfGen1Display = pygwidgets.DisplayText(window,(400 , 45),'0',textColor = WHITE,fontSize = 50)
    numberOfGen2Display = pygwidgets.DisplayText(window,(700 , 45),'0',textColor = WHITE,fontSize = 50)
    numberOfGen3Display = pygwidgets.DisplayText(window,(800 , 55),'0',textColor = WHITE,fontSize = 50)
    cityPowerDemand = pygwidgets.DisplayText(window,(600 , 45), '1', textColor = WHITE , fontSize = 50)

    #Game inventory
    numberOfGenerators1 = 0
    numberOfGenerators2 = 0
    numberOfGenerators3 = 0

    #Demand of city
    cityPowerDemand1 = 45
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if buyGenerator1.handleEvent(event):
                print("Gen button clicked # is" , numberOfGenerators1)
                if numberOfGenerators1 >= 15:
                    print("Max gen owned")
                else:
                    numberOfGenerators1 = numberOfGenerators1 + 1
                    numberOfGen1Display.setValue(numberOfGenerators1)
                

            if buyGenerator2.handleEvent(event):
                print("Gen2 button clicked")
                if numberOfGenerators2 >=15:
                    print("Maxed gen owned")
                else:
                    numberOfGenerators2 = numberOfGenerators2 + 1
                    numberOfGen2Display.setValue(numberOfGenerators2)

            if buyGenerator3.handleEvent(event):
                print("Gen3 button clicked")
                if numberOfGenerators3 >=15:
                    print("Maxed gen owned")
                else:
                    numberOfGenerators3 = numberOfGenerators3 + 1
                    numberOfGen3Display.setValue(numberOfGenerators3)
            

            
        totalPowerOutput = numberOfGenerators1 + numberOfGenerators2 + numberOfGenerators3

        if totalPowerOutput == cityPowerDemand1:
            print("You passed!")
            wonGameScreen()
            #print(totalPowerOutput)
            
                

        window.blit(backGroundImage, (0, 0))
        buyGenerator1.draw()
        buyGenerator2.draw()
        buyGenerator3.draw()
        numberOfGen1Display.draw()
        numberOfGen2Display.draw()
        numberOfGen3Display.draw()
        cityPowerDemand.draw()

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)



def gameLevel2():
    #Buttons to buy generators
    buyGenerator1 = pygwidgets.TextButton(window, (45, 655), 'Buy a generator 1')
    buyGenerator2 = pygwidgets.TextButton(window, (250, 655), 'Buy a generator 2')
    buyGenerator3 = pygwidgets.TextButton(window, (460, 655), 'Buy a generator 3')

    #Display game data
    numberOfGen1Display = pygwidgets.DisplayText(window,(400 , 45),'0',textColor = WHITE,fontSize = 50)
    numberOfGen2Display = pygwidgets.DisplayText(window,(700 , 45),'0',textColor = WHITE,fontSize = 50)
    numberOfGen3Display = pygwidgets.DisplayText(window,(800 , 55),'0',textColor = WHITE,fontSize = 50)
    cityPowerDemand = pygwidgets.DisplayText(window,(600 , 45), '1', textColor = WHITE , fontSize = 50)

    #Game inventory
    numberOfGenerators1 = 0
    numberOfGenerators2 = 0
    numberOfGenerators3 = 0

    #Demand of city
    cityPowerDemand1 = 45

    myDisplay = pygame.display.set_mode((1280 ,720))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if buyGenerator1.handleEvent(event):
                print("Gen button clicked # is" , numberOfGenerators1)
                if numberOfGenerators1 >= 15:
                    print("Max gen owned")
                else:
                    numberOfGenerators1 = numberOfGenerators1 + 1
                    numberOfGen1Display.setValue(numberOfGenerators1)
                

            if buyGenerator2.handleEvent(event):
                print("Gen2 button clicked")
                if numberOfGenerators2 >=15:
                    print("Maxed gen owned")
                else:
                    numberOfGenerators2 = numberOfGenerators2 + 1
                    numberOfGen2Display.setValue(numberOfGenerators2)

            if buyGenerator3.handleEvent(event):
                print("Gen3 button clicked")
                if numberOfGenerators3 >=15:
                    print("Maxed gen owned")
                else:
                    numberOfGenerators3 = numberOfGenerators3 + 1
                    numberOfGen3Display.setValue(numberOfGenerators3)
            

            
        totalPowerOutput = numberOfGenerators1 + numberOfGenerators2 + numberOfGenerators3

        if totalPowerOutput == cityPowerDemand1:
            print("You passed!")
            #print(totalPowerOutput)
            
                

        window.blit(backGroundImage, (0, 0))
        #pygame.draw.rect(myDisplay ,WHITE, [00, 475, 2000, 1000], 65)
        buyGenerator1.draw()
        buyGenerator2.draw()
        buyGenerator3.draw()
        numberOfGen1Display.draw()
        numberOfGen2Display.draw()
        numberOfGen3Display.draw()
        cityPowerDemand.draw()

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)






#Starts game menu
startMenu()
#wonGameScreen()

