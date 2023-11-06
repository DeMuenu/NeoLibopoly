import pygame
import threading
import socket
import time
import pickle

serverip = input("Server Ip eingeben: ")
nr = input("Spielernummer eingeben: ")
deviceName = "PlayerOne"

NewMove = "Test/one"
GameData = {}

def variableRefresh():
    global GameData
    global NewMove
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((serverip, 5345))
    if client.recv(1024).decode("utf-8") == "NICK":
        client.send(deviceName.encode("utf-8"))
        client.send(nr.encode("utf-8"))
    else:
        print("Communication error")
    while True:
        GameData = pickle.loads(client.recv(4056))
        client.send(NewMove.encode("utf-8"))
        rec = client.recv(1024).decode("utf-8")
        #print(GameData)
        for i in GameData["players"]:
            print(i.position)
        #print(variables)
        #print(NewMove)
        #print(rec)
        if rec == NewMove:
            NewMove = "None/None"
            print("same")
        else:
            print("notsame")


thread = threading.Thread(target=variableRefresh, daemon=True)
thread.start()

time.sleep(3)

pygame.init()
ScreenWidth = 1920
ScreenHeight = 1080
zoom = 1
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))


emptyDict = {}
Layer1 = []
Layer2 = []
ClickableObjectsList = []
scale = 1


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

createSomething("1", "assets/board/temp_house.jpg", 100, 100, 200, 200, True)
createSomething("2", "assets/board/temp_house.jpg", 305, 100, 200, 200, True)
createSomething("3", "assets/board/temp_house.jpg", 510, 100, 200, 200, True)
createSomething("4", "assets/board/temp_house.jpg", 715, 100, 200, 200, True)
createSomething("5", "assets/board/temp_house.jpg", 920, 100, 200, 200, True)
createSomething("6", "assets/board/temp_house.jpg", 1125, 100, 200, 200, True)
createSomething("7", "assets/board/temp_house.jpg", 1330, 100, 200, 200, True)
createSomething("8", "assets/board/temp_house.jpg", 1535, 100, 200, 200, True)
createSomething("9", "assets/board/temp_house.jpg", 1740, 100, 200, 200, True)
createSomething("10", "assets/board/temp_house.jpg", 1945, 100, 200, 200, True)
createSomething("11", "assets/board/temp_house.jpg", 2150, 100, 200, 200, True)

createSomething("12", "assets/board/temp_house.jpg", 2150, 305, 200, 200, True)
createSomething("13", "assets/board/temp_house.jpg", 2150, 510, 200, 200, True)
createSomething("14", "assets/board/temp_house.jpg", 2150, 715, 200, 200, True)
createSomething("15", "assets/board/temp_house.jpg", 2150, 920, 200, 200, True)
createSomething("16", "assets/board/temp_house.jpg", 2150, 1125, 200, 200, True)
createSomething("17", "assets/board/temp_house.jpg", 2150, 1330, 200, 200, True)
createSomething("18", "assets/board/temp_house.jpg", 2150, 1535, 200, 200, True)
createSomething("19", "assets/board/temp_house.jpg", 2150, 1740, 200, 200, True)
createSomething("20", "assets/board/temp_house.jpg", 2150, 1945, 200, 200, True)
createSomething("21", "assets/board/temp_house.jpg", 2150, 2150, 200, 200, True)

createSomething("22", "assets/board/temp_house.jpg", 1945, 2150, 200, 200, True)
createSomething("23", "assets/board/temp_house.jpg", 1740, 2150, 200, 200, True)
createSomething("24", "assets/board/temp_house.jpg", 1535, 2150, 200, 200, True)
createSomething("25", "assets/board/temp_house.jpg", 1330, 2150, 200, 200, True)
createSomething("26", "assets/board/temp_house.jpg", 1125, 2150, 200, 200, True)
createSomething("27", "assets/board/temp_house.jpg", 920, 2150, 200, 200, True)
createSomething("28", "assets/board/temp_house.jpg", 715, 2150, 200, 200, True)
createSomething("29", "assets/board/temp_house.jpg", 510, 2150, 200, 200, True)
createSomething("30", "assets/board/temp_house.jpg", 305, 2150, 200, 200, True)
createSomething("31", "assets/board/temp_house.jpg", 100, 2150, 200, 200, True)

createSomething("32", "assets/board/temp_house.jpg", 100, 1945, 200, 200, True)
createSomething("33", "assets/board/temp_house.jpg", 100, 1740, 200, 200, True)
createSomething("34", "assets/board/temp_house.jpg", 100, 1535, 200, 200, True)
createSomething("35", "assets/board/temp_house.jpg", 100, 1330, 200, 200, True)
createSomething("36", "assets/board/temp_house.jpg", 100, 1125, 200, 200, True)
createSomething("37", "assets/board/temp_house.jpg", 100, 920, 200, 200, True)
createSomething("38", "assets/board/temp_house.jpg", 100, 715, 200, 200, True)
createSomething("39", "assets/board/temp_house.jpg", 100, 510, 200, 200, True)
createSomething("40", "assets/board/temp_house.jpg", 100, 305, 200, 200, True)


font = pygame.font.SysFont(None, 24)



RenderedObjectsList = [Layer1, Layer2]
run = True
while run:
    screen.fill((0, 0, 0))
    # pygame.draw.rect(screen, (255, 0, 0), player)
    # screen.blit(board, (900, 500))




    #Render Fields
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

    #Render Players
    for GD in GameData["players"]:
        x = 500
        y = 500
        for i in ClickableObjectsList:
            #print(i)
            #print(GD)
            if i["name"] == str(GD.position):
                y = i["positionY"]
                x = i["positionX"]
                sx =  i["sizeX"] / 4
                sy =  i["sizeY"] / 4
        p = pygame.image.load(f"assets/players/{str(GD.nr)}.png").convert_alpha()
        p = pygame.transform.scale(p, (sx, sy))
        screen.blit(p, (x, y))


    img = font.render(str(GameData["roll"]), True, (255, 0, 0))
    screen.blit(img, (20, 20))

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        for y in RenderedObjectsList:
            for i in y:
                i["positionY"] = i["positionY"] - ( 10 * scale)

        for i in ClickableObjectsList:
            i["positionY"] = i["positionY"] - ( 10 * scale)

    elif key[pygame.K_s] == True:
        for y in RenderedObjectsList:
            for i in y:
                i["positionY"] = i["positionY"] + ( 10 * scale)

        for i in ClickableObjectsList:
            i["positionY"] = i["positionY"] + ( 10 * scale)

    if key[pygame.K_a] == True:
        for y in RenderedObjectsList:
            for i in y:
                i["positionX"] = i["positionX"] - ( 10 * scale)

        for i in ClickableObjectsList:
            i["positionX"] = i["positionX"] - ( 10 * scale)

    elif key[pygame.K_d] == True:
        for y in RenderedObjectsList:
            for i in y:
                i["positionX"] = i["positionX"] + ( 10 * scale)

        for i in ClickableObjectsList:
            i["positionX"] = i["positionX"] + ( 10 * scale)

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
                    NewMove = f"Clicked/{i['name']}"
                    

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



                scale = scale * 1.2




            elif event.y == -1:
                print("Zoomed out")
                for y in RenderedObjectsList:
                    for i in y:
                        i["sizeX"] = i["sizeX"] / 1.2
                        i["sizeY"] = i["sizeY"] / 1.2
                        i["positionX"] = i["positionX"] / 1.2
                        i["positionY"] = i["positionY"] / 1.2
                        
                        #i["object"] = pygame.image.load(i["path"]).convert_alpha()
                        i["object"] = pygame.transform.scale(
                            i["object"], (i["sizeX"], i["sizeY"])
                        )
                        print(i["sizeX"])

                for x in ClickableObjectsList:
                    x["positionX"] = x["positionX"] / 1.2
                    x["positionY"] = x["positionY"] / 1.2
                    x["sizeX"] = x["sizeX"] / 1.2
                    x["sizeY"] = x["sizeY"] / 1.2


                scale = scale / 1.2

    pygame.display.update()


pygame.quit()
