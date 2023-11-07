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

GameData = {"players": players, "roll": 0, "whosTurn": 1}


devicesClients = []  # Always execute
devices = []


def handle(client):  # Update GameData and get the next Move for each player
    while True:
        try:
            # Broadcasting Messages
            client.send(pickle.dumps(GameData))
            message = client.recv(1024).decode("utf-8")
            client.send(message.encode("utf-8"))
            time.sleep(0.2)

            splitMessageCommand, splitMessageData = message.split("/")
            if splitMessageCommand == "clicked":
                for i in GameData["players"]:
                    if message != "None":
                        print(message)
                    if str(i.client) == str(client):
                        if splitMessageData == "roll":
                            random.seed(
                                a=(str(time.localtime())), version=2)
                            GameData["roll"] = random.randrange(1, 12, 1)

                            i.position = i.position + GameData["roll"]

                            if GameData["whosTurn"] == 1:
                                GameData["whosTurn"] = 2
                            else:
                                GameData["whosTurn"] = 1

        except:
            # print("Error: " + str(e))
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
    Playernr = client.recv(1024).decode("utf-8")
    devices.append(nickname)
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
