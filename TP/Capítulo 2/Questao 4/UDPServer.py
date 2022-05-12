from socket import *

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive...\n")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    print(modifiedMessage)