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


def getstatus():
    global Status
    while True:
        try:
            url = "http://ha.heuer-memes.ch/api/states"
            headers = {
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMDIzZWEyNzA2MjQ0ZGZkOWU2ZWEzOWVkZjI2ZTY0OSIsImlhdCI6MTY5NjY0Mjc5NSwiZXhwIjoyMDEyMDAyNzk1fQ.1zhAkc67eEWKR9ahCd9wsRJuh_81MUq2QtCEwcsopZE",
                "content-type": "application/json",
            }

            response = get(url, headers=headers)
            responseText = response.text
            responseData = json.loads(responseText)
            # print(responseData)

            StatusString = ""

            for x in responseData:
                # print(x["entity_id"])
                if x["entity_id"].startswith("switch"):
                    # print(x)
                    StatusString = (
                        StatusString
                        + f"{x['attributes']['friendly_name']}={x['state']} and can be set to: 'on' or 'off'; "
                    )

            # add the time
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d")
            formatted_time = now.strftime("%H:%M:%S")
            print(f"The date is {formatted_date} and the time is {formatted_time}; ")
            StatusString = (
                StatusString
                + f"The date is {formatted_date} and the time is {formatted_time}; "
            )

            print(StatusString)

            Status = StatusString
        except KeyError as e:
            print(e)
            Status = "Error getting status from Home Network"

        time.sleep(15)


gettingstatus = threading.Thread(target=getstatus)
gettingstatus.daemon = True
gettingstatus.start()


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
