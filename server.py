import pickle
import time
from player import playerclass
import threading
import socket
import random


host = "localhost"
port = 5345



#only on gamestart

players = []

GameData = {"players" : players, "roll" : 0}

GameData["players"].append(playerclass(100000, 3, 1))

GameData["players"].append(playerclass(100000, 5, 2))




devicesClients = [] #Always execute
devices = []

def handle(client): #Update GameData and get the next Move for each player
    while True:
        try:
            # Broadcasting Messages
            client.send(pickle.dumps(GameData))
            message = client.recv(1024).decode("utf-8")
            client.send(message.encode("utf-8"))
            time.sleep(0.2)
            if message != "None":
                print(message)

            splitMessageCommand, splitMessageData = message.split("/")
            if splitMessageCommand == "Clicked":
                for i in GameData["players"]:
                    i.position = i.position + 3
                    random.seed(a=(str(client) * str(time.localtime())), version=2)
                    GameData["roll"] = random.randrange(1, 12, 1)
                    print(f"roll = {GameData['roll']}")

        except:
            #print("Error: " + str(e))
            index = devicesClients.index(client)
            devicesClients.remove(client)
            client.close()
            nickname = devices[index]
            devices.remove(nickname)
            print(f"removed {nickname}")
            break
            # client.send(xx.encode("utf-8"))





def gameloop():
    while True:
        for i in GameData["players"]:
            if i.position > 40:
                i.position = i.position - 40
                i.money = i.money + 4000

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
    devices.append(nickname)
    devicesClients.append(client)
    thread = threading.Thread(target=handle, args=(client,)).start()

    print(f"{devices} {devicesClients}")
