import pygame


pygame.init()

ScreenWidth = 1920
ScreenHeight = 1080

screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))


emptyDict = {}
Layer1 = []
Layer2 = []
ClickableObjectsList = []

def addRenderObject(object, Layer, StartPosX, StartPosY, Color):
    if Layer == 1:
        Layer1.append(emptyDict.copy())
        x = Layer1[-1]
    if Layer == 2:
        Layer2.append(emptyDict.copy())
        x = Layer2[-1]
    x["object"] = object
    x["positionX"] = StartPosX
    x["positionY"] = StartPosY
    x["Color"] = Color

def addClickableObject(object, PositionX, PositionY, SizeX, SizeY):
    ClickableObjectsList.append(emptyDict.copy())
    x = ClickableObjectsList[-1]
    x["object"] = object
    x["positionX"] = PositionX
    x["positionY"] = PositionY
    x["SizeX"] = SizeX
    x["SizeY"] = SizeY
#Textures


player = pygame.Rect((300, 250, 50, 50))
addRenderObject(player, 1, 900, 800, (0, 0, 255))


PosNextX = 900
PosNextY = 50
ScaleNextX = 100
ScaleNextY = 100
Board = pygame.image.load('assets/Board/cat.png').convert_alpha()
Board = pygame.transform.scale(Board, (ScaleNextX, ScaleNextY))
addRenderObject(Board, 1, PosNextX, PosNextY, (255, 0, 0))
addClickableObject(Board, PosNextX, PosNextY, ScaleNextX, ScaleNextY)



PosNextX = 900
PosNextY = 500
ScaleNextX = 100
ScaleNextY = 100
Board = pygame.image.load('assets/Board/cat.png').convert_alpha()
Board = pygame.transform.scale(Board, (ScaleNextX, ScaleNextY))
addRenderObject(Board, 1, PosNextX, PosNextY, (255, 0, 0))
addClickableObject(Board, PosNextX, PosNextY, ScaleNextX, ScaleNextY)



RenderedObjectsList = [Layer1, Layer2]
run = True
while run:
    screen.fill((0, 0, 0))
    #pygame.draw.rect(screen, (255, 0, 0), player)
    #screen.blit(Board, (900, 500))

    #walk
    for z in RenderedObjectsList:
        for i in z:
            #print(i)
            if str(i["object"]).startswith("<Surface"):
                #print("Surface")
                screen.blit(i["object"], (i["positionX"], i["positionY"]))

            if str(i["object"]).startswith("<rect"):
                #print("Rect")
                pygame.draw.rect(screen, i["Color"], i["object"])



    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        for y in RenderedObjectsList:
            for i in y:
                i["positionY"] = i["positionY"] - 1

        for i in ClickableObjectsList:
            i["positionY"] = i["positionY"] - 1

    elif key[pygame.K_s] == True:
        for y in RenderedObjectsList:
            for i in y:
                i["positionY"] = i["positionY"] + 1

        for i in ClickableObjectsList:
            i["positionY"] = i["positionY"] + 1

    elif key[pygame.K_a] == True:
        for y in RenderedObjectsList:
            for i in y:
                i["positionX"] = i["positionX"] - 1

        for i in ClickableObjectsList:
            i["positionX"] = i["positionX"] - 1

    elif key[pygame.K_d] == True:
        for y in RenderedObjectsList:
            for i in y:
                i["positionX"] = i["positionX"] + 1

        for i in ClickableObjectsList:
            i["positionX"] = i["positionX"] + 1

    #eventhandler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in ClickableObjectsList:
                print(i)
                MouseX, MouseY = pygame.mouse.get_pos()
                if MouseX >= i["positionX"] and MouseX <= i["positionX"] + i["SizeX"] and MouseY >= i["positionY"] and MouseY <= i["positionY"] + i["SizeY"]:
                    print("Clicked")
                


    pygame.display.update()



pygame.quit()


        