import socket
import datetime
import os

hour= datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second= datetime.datetime.now().second
FORMAT="utf-8"
size=1000
port=9999
host=socket.gethostname()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM )
s.connect((host, port ))
print("you has been connect ")
while 21==21:
    #recv message from server 
    smessage= s.recv(size).decode("utf-8")
    print(f" AT (  {str(hour)}:{str(minute)}:{str(second)} ) server said  : {smessage}")
    #send message to server
    message=input(" client : ")
    s.sendall( message.encode ("utf-8"))
    if message=="quit":
        print("conection if finish")
        break
    
    elif message == "put" :
        osam=input("your file name that you want send ?  ")
        try:
            file = open( osam , "r")
            print("file exist")
            data = file.read()

            # Sending the filename to the server
            s.send( osam .encode(FORMAT))
            msg = s.recv(size).decode(FORMAT)
            print(f"[SERVER]: {msg}")

            # Sending the file data to the server
            s.send(data.encode(FORMAT))
            msg = s.recv(size).decode(FORMAT)
            print(f"[SERVER]: {msg}")
            file.close()
            break

        except IOError:
             print('File not found  ')
             break
       

    elif message == "get" :

        osam=input("plese enter your file name that you want get from server  : ")
        file = open(f"server/{osam}", "r")
        data = file.read()
        # Sending the filename to the server.
        s.send(f"{osam}".encode(FORMAT))
        msg = s.recv(size).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        # Sending the file data to the server
        s.send(data.encode(FORMAT))
        msg = s.recv(size).decode(FORMAT)
        print(f"[SERVER]: {msg}")
        file.close()
        s.close()

    elif message == "ls":
          smessage = s.recv(size).decode("utf-8")
          print(f" AT (  {str(hour)}:{str(minute)}:{str(second)} ) server said  : {smessage}")
          print(os.listdir(smessage))
          break
    
    
    
s.close()
