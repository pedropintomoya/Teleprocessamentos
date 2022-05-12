from ast import While
from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while 1:
    N = input()
    if(N == 'quit'):
        clientSocket.close()
        break
    N = int(N)
    for i in range(N):
        aux = f"[{str(i)}]"
        clientSocket.send(str.encode(aux))  
        