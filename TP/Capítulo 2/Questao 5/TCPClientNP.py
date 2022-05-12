from ast import While
from socket import *
serverName = 'localhost'
serverPort = 12001
while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print('Digite senha e usuario sem virgula (,)')
    message = input('Usuario: ')
    message2 = input('Senha: ')
    messageTupla = message + ',' + message2
    messageTupla = str.encode(messageTupla)
    clientSocket.send(messageTupla)
    modifiedSentence = clientSocket.recv(1024)
    resposta = modifiedSentence.decode()
    print('From Server:', resposta)
    clientSocket.close()