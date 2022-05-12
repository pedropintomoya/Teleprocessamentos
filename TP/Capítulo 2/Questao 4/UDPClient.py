from ast import While
from base64 import encode
from socket import *

from numpy import array
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
    N = input()
    if(N == 'quit'):
        clientSocket.close()
        break
    N = int(N)
    for i in range(N):
        aux = str(i)
        clientSocket.sendto(str.encode(aux),(serverName,serverPort))
    