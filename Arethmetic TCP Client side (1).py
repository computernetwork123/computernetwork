import socket

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect(('localhost',65535))

a=input("Enter 1st number : ")
b=input("Enter 2nd Number : ")

c.send(a.encode())
c.send(b.encode())


c.recv(1024).decode()
