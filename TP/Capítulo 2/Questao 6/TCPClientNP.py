from ast import While
from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while 1:
    message = input()
    messageSTR = str.encode(message)
    clientSocket.send(messageSTR)
    modifiedSentence = clientSocket.recv(1024)
    resposta = modifiedSentence.decode()
    controle, mensagem = resposta[0:3], resposta[3:]
    print(mensagem)
    while(controle == '[0]'):
        modifiedSentence = clientSocket.recv(1024)
        resposta = modifiedSentence.decode()
        controle, mensagem = resposta[0:3], resposta[3:]
        print(mensagem)
    if(controle == '[1]'):
        continue
    elif(controle == '[2]'):
        clientSocket.close()
        break