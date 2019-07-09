import socket

s = socket.socket()
host = 'localhost'
port = 5000

s.connect((host, port))
fileName = 'fileToGet.txt'
s.send(fileName.encode())
readFile = s.recv(1024)
print(readFile.decode())
s.close()