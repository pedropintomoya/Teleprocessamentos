from socket import *

serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive...\n")
while 1:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024)
    auxCodificado = str.encode('[1]Olá! Bem-vindo! Qual o seu nome?')
    connectionSocket.send(auxCodificado)

    sentence = connectionSocket.recv(1024)
    aux = sentence.decode()
    auxCodificado = str.encode('[1]Certo, '+ aux + '! Como posso te ajudar? Digite o número que corresponde á opção desejada:\n1 - Agendar um horário de monitoria\n2 = Listar as próximos atividades da disciplina\n3 - E-mail do professor')
    connectionSocket.send(auxCodificado)

    sentence = connectionSocket.recv(1024)
    aux = int(sentence.decode())
    if(aux == 1):
        auxCodificado = str.encode('[0]Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@@poli.ufrj.br')
        connectionSocket.send(auxCodificado)
    elif (aux == 2):
        auxCodificado = str.encode('[0]Fique atento para as datas das próximas atividades. Confira o que vem por aí!\n\nP1: 2 de mario de 2022\nLista 3: 29 de maio de 2022')
        connectionSocket.send(auxCodificado)
    elif (aux == 3):
        auxCodificado = str.encode('[0]Quer falar com o professor: O e-mail dele é sadoc@dcc.ufrj.br') 
        connectionSocket.send(auxCodificado)
        
    
    auxCodificado = str.encode('[2]Obrigado por utilizar nossos serviços! Até logo!')
    connectionSocket.send(auxCodificado)
    connectionSocket.close()