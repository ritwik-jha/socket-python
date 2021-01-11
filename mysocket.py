import socket
import threading
import os


ip = input('Enter ip of receiver program: ')
port = int(input('Enter port number of receiver program: '))
def get(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    s.bind((ip,port))

    while True:
        x = s.recvfrom(1024)
        sender = x[1][0]
        data = x[0].decode()

        print(sender+" : "+data)



def send(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data = input()
        data = data.encode()
        s.sendto(data,(ip,port))


x1 = threading.Thread(target=get , args=('192.168.43.166',1234))
x2 = threading.Thread(target=send , args=(ip,port))

x1.start()
x2.start()



