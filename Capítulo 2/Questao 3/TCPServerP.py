from socket import *
from threading import Thread

class atendeCliente(Thread):
    def __init__(self, conectionSocket, addr):
        Thread.__init__(self)
        self.conectionSocket = conectionSocket
        self.addr = addr
    
    def run(self) -> None:
        print(self.addr)
        while 1:
            sentence = self.conectionSocket.recv(1024)
            aux = sentence.decode()
            capitalizedSentence = aux.upper()
            auxCodificado = str.encode(capitalizedSentence)
            self.conectionSocket.send(auxCodificado)


serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive...\n")
while 1:
    connectionSocket, addr = serverSocket.accept()
    atendeCliente(connectionSocket, addr).start()