from socket import *
from threading import Thread

class atendeCliente(Thread):
    def __init__(self, addr, message):
        Thread.__init__(self)
        self.addr = addr
        self.message = message
    
    def run(self) -> None:
        print(self.addr)
        modifiedMessage = self.message.decode().upper()
        serverSocket.sendto(str.encode(modifiedMessage), self.addr)



serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive...\n")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    atendeCliente(clientAddress, message).start()