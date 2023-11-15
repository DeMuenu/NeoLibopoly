import pygame
import threading
import socket
import time
import pickle

serverip = input("Server Ip eingeben: ")
nr = input("Spielernummer eingeben: ")
deviceName = "PlayerOne"  # obsolete

posXold = 0
posYold = 0
ClickableObjectsList = [{"positionX": 0, "positionY": 0}]
NewMove = "Test/one"
GameData = {}
scale = 1

OffsetX = 0
OffsetY = 0

emptyDict = {}
Layer1 = []
Layer2 = []

pygame.init()
ScreenWidth = 1920
ScreenHeight = 1080
zoom = 1
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

def addRenderObject(object, Layer, StartPosX, StartPosY, SizeX, SizeY, path):
    if Layer == 1:
        Layer1.append(emptyDict.copy())
        x = Layer1[-1]
    if Layer == 2:
        Layer2.append(emptyDict.copy())
        x = Layer2[-1]
    x["object"] = object
    x["positionX"] = StartPosX
    x["positionY"] = StartPosY
    x["sizeX"] = SizeX
    x["sizeY"] = SizeY
    x["path"] = path


def addClickableObject(name, object, PositionX, PositionY, SizeX, SizeY, isMenuItem):
    ClickableObjectsList.append(emptyDict.copy())
    x = ClickableObjectsList[-1]
    x["name"] = name
    x["object"] = object
    x["positionX"] = PositionX
    x["positionY"] = PositionY
    x["sizeX"] = SizeX
    x["sizeY"] = SizeY
    x["isMenuItem"] = isMenuItem


def createSomething(name, asset, PosNextX, PosNextY, ScaleNextX, ScaleNextY, clickable, isMenuItem):
    tempOB = pygame.image.load(asset).convert_alpha()
    tempOB = pygame.transform.smoothscale(tempOB, (ScaleNextX, ScaleNextY))
    addRenderObject(tempOB, 1, PosNextX, PosNextY,
                    ScaleNextX, ScaleNextY, asset)
    if clickable == True:
        addClickableObject(name, tempOB, PosNextX,
                           PosNextY, ScaleNextX, ScaleNextY, isMenuItem)


# Fields
ClickableObjectsList.clear()

createSomething("1", "assets/board/temp_house.jpg", 100, 100, 200, 200, True, False)
createSomething("2", "assets/board/temp_house.jpg", 305, 100, 200, 200, True, False)
createSomething("3", "assets/board/temp_house.jpg", 510, 100, 200, 200, True, False)
createSomething("4", "assets/board/temp_house.jpg", 715, 100, 200, 200, True, False)
createSomething("5", "assets/board/temp_house.jpg", 920, 100, 200, 200, True, False)
createSomething("6", "assets/board/temp_house.jpg", 1125, 100, 200, 200, True, False)
createSomething("7", "assets/board/temp_house.jpg", 1330, 100, 200, 200, True, False)
createSomething("8", "assets/board/temp_house.jpg", 1535, 100, 200, 200, True, False)
createSomething("9", "assets/board/temp_house.jpg", 1740, 100, 200, 200, True, False)
createSomething("10", "assets/board/temp_house.jpg", 1945, 100, 200, 200, True, False)
createSomething("11", "assets/board/temp_house.jpg", 2150, 100, 200, 200, True, False)

createSomething("12", "assets/board/temp_house.jpg", 2150, 305, 200, 200, True, False)
createSomething("13", "assets/board/temp_house.jpg", 2150, 510, 200, 200, True, False)
createSomething("14", "assets/board/temp_house.jpg", 2150, 715, 200, 200, True, False)
createSomething("15", "assets/board/temp_house.jpg", 2150, 920, 200, 200, True, False)
createSomething("16", "assets/board/temp_house.jpg",
                2150, 1125, 200, 200, True, False)
createSomething("17", "assets/board/temp_house.jpg",
                2150, 1330, 200, 200, True, False)
createSomething("18", "assets/board/temp_house.jpg",
                2150, 1535, 200, 200, True, False)
createSomething("19", "assets/board/temp_house.jpg",
                2150, 1740, 200, 200, True, False)
createSomething("20", "assets/board/temp_house.jpg",
                2150, 1945, 200, 200, True, False)
createSomething("21", "assets/board/temp_house.jpg",
                2150, 2150, 200, 200, True, False)

createSomething("22", "assets/board/temp_house.jpg",
                1945, 2150, 200, 200, True, False)
createSomething("23", "assets/board/temp_house.jpg",
                1740, 2150, 200, 200, True, False)
createSomething("24", "assets/board/temp_house.jpg",
                1535, 2150, 200, 200, True, False)
createSomething("25", "assets/board/temp_house.jpg",
                1330, 2150, 200, 200, True, False)
createSomething("26", "assets/board/temp_house.jpg",
                1125, 2150, 200, 200, True, False)
createSomething("27", "assets/board/temp_house.jpg", 920, 2150, 200, 200, True, False)
createSomething("28", "assets/board/temp_house.jpg", 715, 2150, 200, 200, True, False)
createSomething("29", "assets/board/temp_house.jpg", 510, 2150, 200, 200, True, False)
createSomething("30", "assets/board/temp_house.jpg", 305, 2150, 200, 200, True, False)
createSomething("31", "assets/board/temp_house.jpg", 100, 2150, 200, 200, True, False)

createSomething("32", "assets/board/temp_house.jpg", 100, 1945, 200, 200, True, False)
createSomething("33", "assets/board/temp_house.jpg", 100, 1740, 200, 200, True, False)
createSomething("34", "assets/board/temp_house.jpg", 100, 1535, 200, 200, True, False)
createSomething("35", "assets/board/temp_house.jpg", 100, 1330, 200, 200, True, False)
createSomething("36", "assets/board/temp_house.jpg", 100, 1125, 200, 200, True, False)
createSomething("37", "assets/board/temp_house.jpg", 100, 920, 200, 200, True, False)
createSomething("38", "assets/board/temp_house.jpg", 100, 715, 200, 200, True, False)
createSomething("39", "assets/board/temp_house.jpg", 100, 510, 200, 200, True, False)
createSomething("40", "assets/board/temp_house.jpg", 100, 305, 200, 200, True, False)


def variableRefresh():
    global GameData
    global NewMove
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((serverip, 5345))
    if client.recv(1024).decode("utf-8") == "NICK":
        client.send(nr.encode("utf-8"))
        client.send(nr.encode("utf-8"))
    else:
        print("Communication error")
 
    while True:
        GameData = pickle.loads(client.recv(5000))
        X, Y = pygame.mouse.get_pos()
        X = (X - OffsetX) / scale 
        Y = (Y - OffsetY) / scale 
        sendlist = [NewMove, X, Y]
        client.send(pickle.dumps(sendlist))
    
        rec = client.recv(1024).decode("utf-8")
        print(GameData)
        if rec == NewMove:
            NewMove = "None/None"
            print("same")
        else:
            print("notsame")


thread = threading.Thread(target=variableRefresh, daemon=True)
thread.start()





time.sleep(3)








font = pygame.font.SysFont(None, 24)


RenderedObjectsList = [Layer1, Layer2]
run = True
while run:
    start = time.time()
    screen.fill((0, 0, 0))
    # pygame.draw.rect(screen, (255, 0, 0), player)
    # screen.blit(board, (900, 500))

    # Render Fields
    for z in RenderedObjectsList:
        for i in z:
            # print(i)
            if str(i["object"]).startswith("<Surface"):
                # print("Surface")
                screen.blit(i["object"], (i["positionX"] + OffsetX, i["positionY"] + OffsetY))

    # Render Players
    for GD in GameData["players"]:
        x = 500
        y = 500
        for i in ClickableObjectsList:
            # print(i)
            # print(GD)
            if i["name"] == str(GD.position):
                y = i["positionY"]
                x = i["positionX"]
                sx = i["sizeX"] / 4
                sy = i["sizeY"] / 4
        p = pygame.image.load(
            f"assets/players/{str(GD.nr)}.png").convert_alpha()
        p = pygame.transform.scale(p, (sx, sy))
        screen.blit(p, (x + OffsetX, y + OffsetY))

    # Roll Button
    # print(f"{nr} {GameData['whosTurn']}")
    if int(nr) == int(GameData["whosTurn"]):
        if GameData["hasRolled"] == False:
            # print("roll")
            rollbutton = pygame.draw.rect(
                screen, (255, 0, 0), pygame.Rect(1700, 800, 200, 100))
            flag = False
            for i in ClickableObjectsList:
                if i["name"] == "roll":
                    flag = True
            if flag == False:
                addClickableObject("roll", rollbutton, 1700, 800, 200, 100, True)

        else:
            # print("shouldnt RollClickObject exists")
            rollbutton = pygame.draw.rect(
                screen, (94, 94, 94), pygame.Rect(1700, 800, 200, 100))
            for i in ClickableObjectsList:
                if i["name"] == "roll":
                    index = ClickableObjectsList.index(i)
                    ClickableObjectsList.pop(index)


            endTurnButton = pygame.image.load(f"assets/UI/endTurn.png").convert_alpha()
            flag = False
            for i in ClickableObjectsList:
                if i["name"] == "skip":
                    flag = True
            if flag == False:
                addClickableObject("skip", rollbutton, 1700, 900, 200, 100, True)
            endTurnButton = pygame.transform.scale(endTurnButton, (200, 100))
            screen.blit(endTurnButton, (1700, 920))
        
    else:        
        tempGDX = (GameData["activeMouseX"] * scale) + OffsetX
        tempGDY = (GameData["activeMouseY"] * scale) + OffsetY
        posYold = ((tempGDY - posYold) * 0.04) + posYold
        posXold = ((tempGDX - posXold) * 0.04) + posXold
        mouse = pygame.image.load(f"assets/players/cursor.png").convert_alpha()
        mouse = pygame.transform.scale(mouse, (50, 50))
        screen.blit(mouse, (posXold, posYold))
        for i in ClickableObjectsList:
            if i["name"] == "skip":
                index = ClickableObjectsList.index(i)
                ClickableObjectsList.pop(index)

    # Render number
    img = font.render(str(GameData["roll"]), True, (255, 238, 0))
    img = pygame.transform.smoothscale(img, (70, 70))
    screen.blit(img, (1765, 815))

    #Render Menus
    if GameData["activeMenuSpecs"]["activeMenus"] != None:
        x = 500
        y = 500
        for i in ClickableObjectsList:
            if i["name"] == str(GameData["activeMenuSpecs"]["MenuAtachedTo"]):
                sx = i["sizeX"]
                sy = i["sizeY"]                
                y = i["positionY"] + sy
                x = i["positionX"]
        pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(x + OffsetX, y + OffsetY, 200, 70 * len(GameData["activeMenuSpecs"]["activeMenus"])))
        for i in GameData["activeMenuSpecs"]["activeMenus"]:
            pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(x + 5 + OffsetX, y + 10 + OffsetY, 190, 50))
            img = font.render(i["OptionText"], True, (255, 238, 0))
            img = pygame.transform.smoothscale(img, (180, 40))
            screen.blit(img, (x + 10 + OffsetX, y + 15 + OffsetY))
            y = y + 70




    # Keypress events
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        OffsetY = OffsetY - (10 * scale)

    elif key[pygame.K_s] == True:
        OffsetY = OffsetY + (10 * scale)

    if key[pygame.K_a] == True:
        OffsetX = OffsetX - (10 * scale)

    elif key[pygame.K_d] == True:
        OffsetX = OffsetX + (10 * scale)

    if key[pygame.K_ESCAPE] == True:
        run = False

    # eventhandler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in ClickableObjectsList:
                # print(i)
                MouseX, MouseY = pygame.mouse.get_pos()
                if i["isMenuItem"] == True:
                    if (
                        MouseX >= i["positionX"]
                        and MouseX <= i["positionX"] + i["sizeX"]
                        and MouseY >= i["positionY"]
                        and MouseY <= i["positionY"] + i["sizeY"]
                    ):
                        print(f"Clicked {i['name']}")
                        NewMove = f"clicked/{i['name']}"
                else:
                    if (
                        MouseX >= i["positionX"] + OffsetX
                        and MouseX <= i["positionX"] + i["sizeX"] + OffsetX
                        and MouseY >= i["positionY"] + OffsetY
                        and MouseY <= i["positionY"] + i["sizeY"] + OffsetY
                    ):
                        print(f"Clicked {i['name']}")
                        NewMove = f"clicked/{i['name']}"

        zoomold = zoom
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                print("Zoomed in")
                for y in RenderedObjectsList:
                    for i in y:
                        i["sizeX"] = i["sizeX"] * 1.2
                        i["sizeY"] = i["sizeY"] * 1.2
                        i["positionX"] = i["positionX"] * 1.2
                        i["positionY"] = i["positionY"] * 1.2
                        i["object"] = pygame.image.load(
                            i["path"]).convert_alpha()
                        i["object"] = pygame.transform.scale(
                            i["object"], (i["sizeX"], i["sizeY"])
                        )

                for x in ClickableObjectsList:
                    if x["name"] != "roll":
                        x["positionX"] = x["positionX"] * 1.2
                        x["positionY"] = x["positionY"] * 1.2
                        x["sizeX"] = x["sizeX"] * 1.2
                        x["sizeY"] = x["sizeY"] * 1.2

                scale = scale * 1.2

            elif event.y == -1:
                print("Zoomed out")
                for y in RenderedObjectsList:
                    for i in y:
                        i["sizeX"] = i["sizeX"] / 1.2
                        i["sizeY"] = i["sizeY"] / 1.2
                        i["positionX"] = i["positionX"] / 1.2
                        i["positionY"] = i["positionY"] / 1.2

                        # i["object"] = pygame.image.load(i["path"]).convert_alpha()
                        i["object"] = pygame.transform.scale(
                            i["object"], (i["sizeX"], i["sizeY"])
                        )
                        print(i["sizeX"])

                for x in ClickableObjectsList:
                    if x["name"] != "roll":
                        x["positionX"] = x["positionX"] / 1.2
                        x["positionY"] = x["positionY"] / 1.2
                        x["sizeX"] = x["sizeX"] / 1.2
                        x["sizeY"] = x["sizeY"] / 1.2

                scale = scale / 1.2
    end = time.time()
    fps = (end-start)
    fps = 1/fps
    img = font.render(str(round(fps)), True, (255, 255, 25))
    screen.blit(img, (20, 20))
    pygame.display.update()


pygame.quit()
