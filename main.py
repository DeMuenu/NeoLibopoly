import pygame
import threading
import socket
import time

serverip = input("Server Ip eingeben: ")
deviceName = "PlayerOne"

NewMove = "Test"


def variableRefresh():
    global NewMove
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((serverip, 5345))
    if client.recv(1024).decode("utf-8") == "NICK":
        client.send(deviceName.encode("utf-8"))
    else:
        print("Communication error")
    while True:
        variables = client.recv(1024).decode("utf-8")
        client.send(NewMove.encode("utf-8"))
        rec = client.recv(1024).decode("utf-8")
        print(variables)
        print(NewMove)
        print(rec)
        if rec == NewMove:
            NewMove = "None"
            print("same")
        else:
            print("notsame")


thread = threading.Thread(target=variableRefresh, daemon=True)
thread.start()


pygame.init()
ScreenWidth = 1920
ScreenHeight = 1080
zoom = 1
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))


emptyDict = {}
Layer1 = []
Layer2 = []
ClickableObjectsList = []


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


def addClickableObject(name, object, PositionX, PositionY, SizeX, SizeY):
    ClickableObjectsList.append(emptyDict.copy())
    x = ClickableObjectsList[-1]
    x["name"] = name
    x["object"] = object
    x["positionX"] = PositionX
    x["positionY"] = PositionY
    x["sizeX"] = SizeX
    x["sizeY"] = SizeY


def createSomething(name, asset, PosNextX, PosNextY, ScaleNextX, ScaleNextY, clickable):
    tempOB = pygame.image.load(asset).convert_alpha()
    tempOB = pygame.transform.smoothscale(tempOB, (ScaleNextX, ScaleNextY))
    addRenderObject(tempOB, 1, PosNextX, PosNextY, ScaleNextX, ScaleNextY, asset)
    if clickable == True:
        addClickableObject(name, tempOB, PosNextX, PosNextY, ScaleNextX, ScaleNextY)


# Fields

createSomething("Feld1", "assets/Board/temp_house.jpg", 100, 100, 200, 200, True)
createSomething("Feld2", "assets/Board/temp_house.jpg", 305, 100, 200, 200, True)
createSomething("Feld3", "assets/Board/temp_house.jpg", 510, 100, 200, 200, True)
createSomething("Feld4", "assets/Board/temp_house.jpg", 715, 100, 200, 200, True)
createSomething("Feld5", "assets/Board/temp_house.jpg", 920, 100, 200, 200, True)
createSomething("Feld6", "assets/Board/temp_house.jpg", 1125, 100, 200, 200, True)
createSomething("Feld7", "assets/Board/temp_house.jpg", 1330, 100, 200, 200, True)
createSomething("Feld8", "assets/Board/temp_house.jpg", 1535, 100, 200, 200, True)
createSomething("Feld9", "assets/Board/temp_house.jpg", 1740, 100, 200, 200, True)
createSomething("Feld10", "assets/Board/temp_house.jpg", 1945, 100, 200, 200, True)
createSomething("Feld11", "assets/Board/temp_house.jpg", 2150, 100, 200, 200, True)

createSomething("Feld12", "assets/Board/temp_house.jpg", 2150, 305, 200, 200, True)
createSomething("Feld13", "assets/Board/temp_house.jpg", 2150, 510, 200, 200, True)
createSomething("Feld14", "assets/Board/temp_house.jpg", 2150, 715, 200, 200, True)
createSomething("Feld15", "assets/Board/temp_house.jpg", 2150, 920, 200, 200, True)
createSomething("Feld16", "assets/Board/temp_house.jpg", 2150, 1125, 200, 200, True)
createSomething("Feld17", "assets/Board/temp_house.jpg", 2150, 1330, 200, 200, True)
createSomething("Feld18", "assets/Board/temp_house.jpg", 2150, 1535, 200, 200, True)
createSomething("Feld19", "assets/Board/temp_house.jpg", 2150, 1740, 200, 200, True)
createSomething("Feld20", "assets/Board/temp_house.jpg", 2150, 1945, 200, 200, True)
createSomething("Feld21", "assets/Board/temp_house.jpg", 2150, 2150, 200, 200, True)

createSomething("Feld22", "assets/Board/temp_house.jpg", 1945, 2150, 200, 200, True)
createSomething("Feld23", "assets/Board/temp_house.jpg", 1740, 2150, 200, 200, True)
createSomething("Feld24", "assets/Board/temp_house.jpg", 1535, 2150, 200, 200, True)
createSomething("Feld25", "assets/Board/temp_house.jpg", 1330, 2150, 200, 200, True)
createSomething("Feld26", "assets/Board/temp_house.jpg", 1125, 2150, 200, 200, True)
createSomething("Feld27", "assets/Board/temp_house.jpg", 920, 2150, 200, 200, True)
createSomething("Feld28", "assets/Board/temp_house.jpg", 715, 2150, 200, 200, True)
createSomething("Feld29", "assets/Board/temp_house.jpg", 510, 2150, 200, 200, True)
createSomething("Feld30", "assets/Board/temp_house.jpg", 305, 2150, 200, 200, True)
createSomething("Feld31", "assets/Board/temp_house.jpg", 100, 2150, 200, 200, True)

createSomething("Feld32", "assets/Board/temp_house.jpg", 100, 1945, 200, 200, True)
createSomething("Feld33", "assets/Board/temp_house.jpg", 100, 1740, 200, 200, True)
createSomething("Feld34", "assets/Board/temp_house.jpg", 100, 1535, 200, 200, True)
createSomething("Feld35", "assets/Board/temp_house.jpg", 100, 1330, 200, 200, True)
createSomething("Feld36", "assets/Board/temp_house.jpg", 100, 1125, 200, 200, True)
createSomething("Feld37", "assets/Board/temp_house.jpg", 100, 920, 200, 200, True)
createSomething("Feld38", "assets/Board/temp_house.jpg", 100, 715, 200, 200, True)
createSomething("Feld39", "assets/Board/temp_house.jpg", 100, 510, 200, 200, True)
createSomething("Feld40", "assets/Board/temp_house.jpg", 100, 305, 200, 200, True)


RenderedObjectsList = [Layer1, Layer2]
run = True
while run:
    screen.fill((0, 0, 0))
    # pygame.draw.rect(screen, (255, 0, 0), player)
    # screen.blit(Board, (900, 500))

    # walk
    for z in RenderedObjectsList:
        for i in z:
            # print(i)
            if str(i["object"]).startswith("<Surface"):
                # print("Surface")
                screen.blit(i["object"], (i["positionX"], i["positionY"]))

            # obsolete
            if str(i["object"]).startswith("<rect"):
                # print("Rect")
                pygame.draw.rect(screen, i["Color"], i["object"])
            # obsolete

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

    if key[pygame.K_a] == True:
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
                if (
                    MouseX >= i["positionX"]
                    and MouseX <= i["positionX"] + i["sizeX"]
                    and MouseY >= i["positionY"]
                    and MouseY <= i["positionY"] + i["sizeY"]
                ):
                    print(f"Clicked {i['name']}")
                    NewMove = f"Clicked {i['name']}"
                    

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
                        i["object"] = pygame.image.load(i["path"]).convert_alpha()
                        i["object"] = pygame.transform.scale(
                            i["object"], (i["sizeX"], i["sizeY"])
                        )

                for x in ClickableObjectsList:
                    x["positionX"] = x["positionX"] * 1.2
                    x["positionY"] = x["positionY"] * 1.2
                    x["sizeX"] = x["sizeX"] * 1.2
                    x["sizeY"] = x["sizeY"] * 1.2

            elif event.y == -1:
                print("Zoomed out")
                for y in RenderedObjectsList:
                    for i in y:
                        i["sizeX"] = i["sizeX"] / 1.2
                        i["sizeY"] = i["sizeY"] / 1.2
                        i["positionX"] = i["positionX"] / 1.2
                        i["positionY"] = i["positionY"] / 1.2
                        i["object"] = pygame.image.load(i["path"]).convert_alpha()
                        i["object"] = pygame.transform.scale(
                            i["object"], (i["sizeX"], i["sizeY"])
                        )
                        print(i["sizeX"])

                for x in ClickableObjectsList:
                    x["positionX"] = x["positionX"] / 1.2
                    x["positionY"] = x["positionY"] / 1.2
                    x["sizeX"] = x["sizeX"] / 1.2
                    x["sizeY"] = x["sizeY"] / 1.2

    pygame.display.update()


pygame.quit()
