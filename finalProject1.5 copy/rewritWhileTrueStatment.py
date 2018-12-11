

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if state == 0    
                if start.handleEvent(event):
                    print("Start")
                    gameLevel1()

                    if quitGame.handleEvent(event):
                    print("quit")
                    pygame.quit()
                    quit()
                state =+ 1
            if state == 1:
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

        

        if state == 2:
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

        if totalPowerOutput == cityPowerDemand1:
            print("You passed!")
            wonGameScreen()
            

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










        window.blit(startMenu, (0, 0))
        start.draw()
        quitGame.draw()

        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)
