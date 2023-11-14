import pickle
import time
from player import playerclass
import threading
import socket
import random


host = "localhost"
port = 5345


# only on gamestart

players = []
active_players = []

activeMenus = [{"OptionText": "Buy Field", "OptionFunction": "buyField"}]
activeMenuSpecs = {"MenuAtachedTo": "4", "activeMenus": activeMenus}

GameData = {"players": players, "roll": 0,
            "whosTurn": 1, "aktivePlayers": active_players, "hasRolled": False, "activeMouseX": 0, "activeMouseY": 0, "activeMenuSpecs" : activeMenuSpecs}


devicesClients = []  # Always execute
devices = []


def handle(client):  # Update GameData and get the next Move for each player
    while True:
        try:
            # Broadcasting Messages
            client.send(pickle.dumps(GameData))
            list = pickle.loads(client.recv(1024))
            message, MouseX, MouseY = list
                        
            client.send(message.encode("utf-8"))
            time.sleep(0.2)
            index = devicesClients.index(client)
            nickname = devices[index]

            if GameData["whosTurn"] == int(nickname):
                print(MouseX)
                print(MouseY)
                GameData["activeMouseX"] = MouseX
                GameData["activeMouseY"] = MouseY

            splitMessageCommand, splitMessageData = message.split("/")
            if splitMessageCommand == "clicked":
                for i in GameData["players"]:

                    if str(i.client) == str(client):
                        print(f"{i.nr} {GameData['whosTurn']}")
                        if int(i.nr) == int(GameData["whosTurn"]):
                            if splitMessageData == "roll":
                                random.seed(
                                    a=(str(time.localtime())), version=2)
                                GameData["roll"] = random.randrange(2, 12, 1)

                                i.position = i.position + GameData["roll"]
                                GameData["hasRolled"] = True

                            elif splitMessageData == "skip":
                                if GameData["whosTurn"] == 1:
                                    GameData["whosTurn"] = 2
                                else:
                                    GameData["whosTurn"] = 1
                                GameData["hasRolled"] = False

                            else:
                                GameData["activeMenuSpecs"]["MenuAtachedTo"] = splitMessageData
            

                    

        except:
            # 
            index = devicesClients.index(client)
            devicesClients.remove(client)
            client.close()
            nickname = devices[index]
            devices.remove(nickname)
            GameData["aktivePlayers"].remove(nickname)
            print(f"removed {nickname}")
            
            # client.send(xx.encode("utf-8"))
            #print("Error: " + str(e))
            break


def gameloop():
    counter = 0
    while True:
        for i in GameData["players"]:
            if i.position > 40:
                i.position = i.position - 40
                i.money = i.money + 4000
        #print(GameData["aktivePlayers"])
        time.sleep(0.2)


thread = threading.Thread(target=gameloop).start()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# keepalive.set(server)

while True:
    client, address = server.accept()

    client.send("NICK".encode("utf-8"))
    nickname = client.recv(1024).decode("utf-8")
    Playernr = client.recv(1024).decode("utf-8")
    devices.append(nickname)
    GameData["aktivePlayers"].append(nickname)
    devicesClients.append(client)
    flag = 0
    for i in GameData["players"]:
        if i.nr == Playernr:
            i.client = str(client)
            flag = 1

    if flag == 0:
        GameData["players"].append(playerclass(
            100000, 1, str(client), Playernr))

    thread = threading.Thread(target=handle, args=(client,)).start()

    print(f"{devices} {devicesClients}")
