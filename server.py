import socket
import datetime
import os
# for time
hour= datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second= datetime.datetime.now().second
SIZE = 1000
port=9999
FORMAT = "utf-8"
host=socket.gethostname()
# make object of socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM )

s.bind((host, port ))

s.listen(5)
print(" I'm waiting for the client to connect")
# Accept requests to connect
client , address = s.accept()
print(f"connection from {address} has been connect")


while 21==21:
    # send text message
    message=input(" server : ")
    client.sendall(message.encode(FORMAT))
    #recv text message
    cmessage=client.recv(SIZE).decode("utf-8")
    print(f"({str(hour)}:{str(minute)}:{str(second)}){cmessage}")
    # quit command
    if cmessage == "quit" :
        print("conection if finish")
        break
    # put  command
    elif cmessage=="put":
        # get file_name from client  for upload
        filename = client.recv(SIZE).decode(FORMAT)
        file = open(filename, "w")
        client.send(f"{filename} is the file name .".encode(FORMAT))

        # get the file from client
        data = client.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        client.send(f"{filename} is the file and reciveed .".encode(FORMAT))
        file.close()

        client.close()
        print(f" {address} disconnected.")
        break
    # get  command
    elif cmessage=="get":
      while 21==21:
        # get file_name from client  for upload
        filename = client.recv(SIZE).decode(FORMAT)
        file = open(filename, "w")
        client.sendall(f"{filename} is the file and transform .".encode(FORMAT))
        data = client.recv(SIZE).decode(FORMAT)
        print(f"{filename} tranform ")
        file.write(data)
        client.sendall("the file data from the client.".encode(FORMAT))
        file.close()
        client.close()
        print(f"[DISclientECTED] {address} disclientected.")


    # list command
    elif cmessage == "ls":
         path = os.getcwd()
         client.sendall(path.encode(FORMAT))
         break



client.close()


