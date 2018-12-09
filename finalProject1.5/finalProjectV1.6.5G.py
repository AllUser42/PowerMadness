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


#Load Image/assets
startMenu = pygame.image.load("menuPlaceHolderGame.jpg")
backGroundImage = pygame.image.load("images/background.jpg")
city1ImageList = [pygame.image.load("PowerImages/CityPic/city1NoPower.jpg"),pygame.image.load("PowerImages/CityPic/city1MedPower.jpg"),pygame.image.load("PowerImages/CityPic/city1MaxPower.jpg")]
##city2ImageList = [pygame.image.load("PowerImages/CityPic/city2NoPower"),pygame.image.load("PowerImages/CityPic/city2MedPower"),pygame.image.load("PowerImages/CityPic/city2MaxPower")]
##cIty3ImageList = [pygame.image.load("PowerImages/CityPic/lasVegasNoPower",pygame.image.load("PowerImages/CityPic/lasVegasMedPower",pygame.image.load("PowerImages/CityPic/lasVegasMaxPower")]

pygame.mixer.music.load('music/music1.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def sound():
    effect = pygame.mixer.Sound('sounds/bonus.wav')
    effect.play()


def sound2():
    effect = pygame.mixer.Sound('sounds/Nextbutton.wav')
    effect.play()


#Levels
START = 'start'
LEVEL_ONE = 'level one'
LEVEL_TWO = 'level two'
LEVEL_THREE = 'level three'
PLYAER_WON = 'win screen'
PLAYER_LOST = 'lost screen'

#Buttons
startGame = pygwidgets.TextButton(window, (45, 655), 'start game')

buyGenerator1 = pygwidgets.TextButton(window, (55, 655), 'Buy a generator 1')
buyGenerator2 = pygwidgets.TextButton(window, (250, 655), 'Buy a generator 2')
buyGenerator3 = pygwidgets.TextButton(window, (460, 655), 'Buy a generator 3')


#Display game data
numberOfGen1Display = pygwidgets.DisplayText(window,(350 , 45),'0',textColor = WHITE,fontSize = 50)
numberOfGen2Display = pygwidgets.DisplayText(window,(430 , 45),'0',textColor = WHITE,fontSize = 50)
numberOfGen3Display = pygwidgets.DisplayText(window,(510 , 45),'0',textColor = WHITE,fontSize = 50)
totalPowerOutputDisplay = pygwidgets.DisplayText(window,(1000 , 45),'0',textColor = WHITE,fontSize = 50)
playerMoneyDisplay = pygwidgets.DisplayText(window,(750 , 45),'0',textColor = WHITE,fontSize = 50)


#Images chcange
#cityImage = pygwidgets.ImageCollection(window, (100, 200),\
                                     #{‘image1’:’images/SomeImage.png’, ‘image2’:’images/Image2.png’, ‘image3’:’images/Image3.png’}, ‘image1’)



#Generator inventory
numberOfGenerators1 = 0
numberOfGenerators2 = 0
numberOfGenerators3 = 0

playerMoney = 0 

#Random numbers






state = START

#Main loop

while True:

    removeRandomAmount = random.randrange(0,10)

    
    if state == START:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if startGame.handleEvent(event):
                print('start game')
                sound2()
                pygame.mixer.music.play()
                state = LEVEL_ONE
            



            
        window.blit(startMenu, (0, 0))
        startGame.draw()
        #cityImage.draw()
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)

    elif state == LEVEL_ONE or state == LEVEL_TWO or state == LEVEL_THREE:
        if state == LEVEL_ONE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if buyGenerator1.handleEvent(event):
                    print("Gen button clicked # is" , numberOfGenerators1)
                    if numberOfGenerators1 >= 15:
                        sound2()
                        print("Max gen owned")
                    else:
                        sound()
                        numberOfGenerators1 = numberOfGenerators1 + 1
                        numberOfGen1Display.setValue(numberOfGenerators1)
                        playerMoney = playerMoney - 1
                        print(playerMoney)
                        
                
                if buyGenerator2.handleEvent(event):
                    print("Gen2 button clicked")
                    if numberOfGenerators2 >=15:
                        sound2()
                        print("Maxed gen owned")
                    else:
                        sound()
                        numberOfGenerators2 = numberOfGenerators2 + 1
                        numberOfGen2Display.setValue(numberOfGenerators2)
                        

                if buyGenerator3.handleEvent(event):
                    print("Gen3 button clicked")
                    if numberOfGenerators3 >=15:
                        sound2()
                        print("Maxed gen owned")
                    else:
                        sound()
                        numberOfGenerators3 = numberOfGenerators3 + 1
                        numberOfGen3Display.setValue(numberOfGenerators3)


            totalPowerOutput = (numberOfGenerators1) + (numberOfGenerators2 * 4) + (numberOfGenerators3 * 8)

            #in range(0,201):


            if totalPowerOutput >= 5:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 10:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 15:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 20:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 25:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 30:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 35:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 40:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 45:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 50:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 55:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 60:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 65:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 70:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 75:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 80:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 85:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 90:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 95:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 100:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 105:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 110:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 115:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 120:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 125:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 130:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 135:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 140:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 145:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 150:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 155:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 160:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 165:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 170:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 175:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 180:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 185:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 190:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 195:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
            elif totalPowerOutput >= 200:
                totalPowerOutput = totalPowerOutput - removeRandomAmount
 

            totalPowerOutputDisplay.setValue(totalPowerOutput)

            playerMoneyDisplay.setValue(playerMoney)

            if totalPowerOutput == 200:
                print('You passed')

            if totalPowerOutput >= 0:
                

            
                window.blit(backGroundImage,(0,0))
                window.blit(city1ImageList[0],(585,174))
                buyGenerator1.draw()
                buyGenerator2.draw()
                buyGenerator3.draw()
                
                numberOfGen1Display.draw()
                numberOfGen2Display.draw()
                numberOfGen3Display.draw()

                totalPowerOutputDisplay.draw()
                playerMoneyDisplay.draw()



                pygame.display.update()
                clock.tick(FRAMES_PER_SECOND)

            if totalPowerOutput >= 20:
                

            
                window.blit(backGroundImage,(0,0))
                window.blit(city1ImageList[1],(585,174))
                buyGenerator1.draw()
                buyGenerator2.draw()
                buyGenerator3.draw()
                
                numberOfGen1Display.draw()
                numberOfGen2Display.draw()
                numberOfGen3Display.draw()

                totalPowerOutputDisplay.draw()
                playerMoneyDisplay.draw()



                pygame.display.update()
                clock.tick(FRAMES_PER_SECOND)


            if totalPowerOutput >= 70:
                

            
                window.blit(backGroundImage,(0,0))
                window.blit(city1ImageList[2],(585,174))
                buyGenerator1.draw()
                buyGenerator2.draw()
                buyGenerator3.draw()
                
                numberOfGen1Display.draw()
                numberOfGen2Display.draw()
                numberOfGen3Display.draw()

                totalPowerOutputDisplay.draw()
                playerMoneyDisplay.draw()



                pygame.display.update()
                clock.tick(FRAMES_PER_SECOND)


            

            
        
                
