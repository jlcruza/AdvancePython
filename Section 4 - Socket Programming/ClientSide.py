import socket

s = socket.socket()
host = 'localhost'
port = 5000

s.connect((host, port))
message = s.recv(1024)

while message:
    print("Message", message.decode())
    message = s.recv(1024)

s.close()