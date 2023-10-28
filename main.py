import pygame


pygame.init()

ScreenWidth = 1920
ScreenHeight = 1080

screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))



Layer1 = []
Layer2 = []
ClickableObjectsList = []

def addRenderObject(object, Layer, StartPosX, StartPosY, Color):
    if Layer == 1:
        Layer1.append(emptyDict.copy())
        x = Layer1[-1]
    x["object"] = object
    x["positionX"] = StartPosX
    x["positionY"] = StartPosY
    x["Color"] = Color


#Textures
emptyDict = {}

player = pygame.Rect((300, 250, 50, 50))
addRenderObject(player, 1, 900, 800, (0, 0, 255))


Board = pygame.image.load('assets/Board/cat.png').convert_alpha()
addRenderObject(Board, 1, 900, 50, (255, 0, 0))
ClickableObjectsList.append(Board)



RenderedObjectsList = [Layer1, Layer2]
run = True
while run:
    screen.fill((0, 0, 0))
    #pygame.draw.rect(screen, (255, 0, 0), player)
    #screen.blit(Board, (900, 500))

    #walk
    for z in RenderedObjectsList:
        for i in z:
            print(i)
            if str(i["object"]).startswith("<Surface"):
                print("Surface")
                screen.blit(i["object"], (i["positionX"], i["positionY"]))

            if str(i["object"]).startswith("<rect"):
                print("Rect")
                pygame.draw.rect(screen, i["Color"], i["object"])



    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)

    #eventhandler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in ClickableObjectsList:
                if i.get_rect().collidepoint(pygame.mouse.get_pos()):
                    print("Pressed Clickable Object")


    pygame.display.update()



pygame.quit()


        