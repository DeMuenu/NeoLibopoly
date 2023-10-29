import json

data_string = json.dumps("testlol")  # data serialized
data_loaded = json.loads(data_string)
print(data_loaded)


import threading
import socket

devicesClients = []
devices = []


def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024).decode("utf-8")
            print(message)

        except:
            index = devicesClients.index(client)
            devicesClients.remove(client)
            client.close()
            nickname = devices[index]
            devices.remove(nickname)
            print(f"removed {nickname}")
            break
            # client.send(xx.encode("utf-8"))


host = "localhost"
port = 5345

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
