import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bound = False
port = 8000
while not bound:
    try:
        serversocket.bind(("", port))
        bound = True
    except:
        port += 1
print("Port:", port)

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            user_id = self.sock.recv(1024).decode()
            user_message = self.sock.recv(1024).decode()
            print(user_id+" -> "+user_message)
            self.sock.send(b"Received")


serversocket.listen(5)
print ("Server Started\n")
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)