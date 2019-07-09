import socket

host = 'localhost'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print("Listening for request ", port)
con, address = s.accept()
print("Connection has benn established from ", str(address))
try:
    fileName = con.recv((1024))
    file = open(fileName, 'rb')
    readFile = file.read()
    con.send(readFile)
    file.close()
    con.close()
except:
    con.send("File not Found".encode())