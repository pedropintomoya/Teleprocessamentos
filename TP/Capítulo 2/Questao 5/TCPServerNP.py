from socket import *

serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive...\n")
user = ['pedro', 'giovani', 'clara']
senha = ['123', 'asd123', 'batata']
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    aux = sentence.decode()
    useraux, passaux = aux.split(',')
    try:
        N = user.index(useraux)
        if(passaux == senha[N]):
            mensagem = "parabens voce entrou"   
        else: 
            raise Exception
    except:
        mensagem = "senha ou usuario incorretos" 
    finally:
        auxCodificado = str.encode(mensagem)
        connectionSocket.send(auxCodificado)
        connectionSocket.close()