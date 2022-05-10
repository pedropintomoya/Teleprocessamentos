from ast import While
from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while 1:
    message = input('Input lowercase sentence: ')
    if(message == 'quit'):
        clientSocket.close()
        break
    messageSTR = str.encode(message)
    clientSocket.send(messageSTR)
    modifiedSentence = clientSocket.recv(1024)
    resposta = modifiedSentence.decode()
    print('From Server:', resposta)
