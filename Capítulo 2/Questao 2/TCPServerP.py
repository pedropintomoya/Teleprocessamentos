from socket import *

serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive...\n")
connectionSocket, addr = serverSocket.accept()
while 1:
    sentence = connectionSocket.recv(1024)
    aux = sentence.decode()
    capitalizedSentence = aux.upper()
    auxCodificado = str.encode(capitalizedSentence)
    connectionSocket.send(auxCodificado)