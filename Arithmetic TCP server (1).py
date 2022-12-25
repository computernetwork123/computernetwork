import socket

s=socket.socket()
print("Socket Created...")

s.bind(('localhost',65535))

s.listen()

print("Waiting for connections")

while True:

    c, addr=s.accept()

    print("connected with ",addr)
    a=c.recv(1024).decode()
    b=c.recv(1024).decode()
    var1=int(a)
    var2=int(b)
    print("Addition : ",(var1+var2))
    print("Substraction : ", (var1 - var2))
    print("Division : ", (var1 / var2))
    print("Multiplication : ", (var1 * var2))

    c.send("See Results at server side...".encode())
