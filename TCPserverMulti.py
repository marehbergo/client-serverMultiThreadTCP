# -*- coding: utf-8 -*-

# Objetivo : Servidor para envio/recebimento de arquivos
# --------------------------------------------------------
# Entrada : Um nome de arquivo
# Saida : Um possivel arquivo
# Autora : Maria Emilia Bergo - mariaemilia.bergo@gmail.com (adaptado de f_Candido)

from socket import *
import thread
import os

host = ''     # Endereco IP do Servidor
port = 12000  # Porta que o Servidor esta

def conectado(con, cliente):
    print 'Conectado com', cliente[0], 'na porta', cliente[1], '...'

    while True:
        msg = con.recv(5120)
        if not msg: break
        
        dados = msg.split(' ')
        arquivo = dados[0]
        diretorio = dados[1]

        print 'servidor', arquivo, 'porta', cliente[1]
        #print 'servidor', msg, 'porta', cliente[1]

        #lista = os.listdir('/home/marehbergo/Documentos/tp_REDES')
        lista = os.listdir(diretorio)
        
        # Procurando o arquivo na pasta
        for i in lista:
            if arquivo not in lista: 
            # ou
            #if msg not in lista: 
                texto = '\033[31m'+'ERRO: Arquivo buscado não foi encontrado'+'\033[0;0m'
                break
            
            else:
                # Lendo o arquivo do fileSystem
                
                #fileOpen = open(msg, "r")
                # ou
                fileOpen = open(arquivo, "r")
                texto = fileOpen.read()
                fileOpen.close()
                break
        
        con.sendall(texto)

    print 'Finalizando conexao do cliente', cliente
    con.close()
    thread.exit()

serverSocket = socket(AF_INET, SOCK_STREAM)

print '\033[32m'+'\nServidor ativo. Aguardando conexão...'+'\033[0;0m'

orig = (host, port)

serverSocket.bind(orig)
serverSocket.listen(1)

while True:
    con, cliente = serverSocket.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

serverSocket.close()