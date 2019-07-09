import socket

host = 'localhost'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print("Listening for request ", port)
con, address = s.accept()

print("Connection has benn established from ", str(address))
con.send("Hello My name is Alienware and I am the Server".encode())
con.close()