import socket

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("port", type=int)
args = parser.parse_args()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = args.port
s.connect((host,port))

user_id = input("Enter your username: ")

def send_message(message, user_id):
	s.send(user_id.encode()) 
	s.send(message.encode())
	server_data = ''
	server_data = s.recv(1024).decode()
	print(server_data)

while 2:
   message = input()
   send_message(message, user_id)

s.close ()