from ast import While
from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
    message = input('Input lowercase sentence: ')
    if(message == 'quit'):
        clientSocket.close()
        break
    clientSocket.sendto(str.encode(message), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
