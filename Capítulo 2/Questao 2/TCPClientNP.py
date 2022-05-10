from ast import While
from socket import *
serverName = 'localhost'
serverPort = 12001
while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    message = input('Input lowercase sentence: ')
    messageSTR = str.encode(message)
    clientSocket.send(messageSTR)
    modifiedSentence = clientSocket.recv(1024)
    resposta = modifiedSentence.decode()
    print('From Server:', resposta)
    clientSocket.close()