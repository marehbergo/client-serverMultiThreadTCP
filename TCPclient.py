# -*- coding: utf-8 -*-

# Cliente para envio/recebimento de arquivos
# -----------------------------------------------------
# Entrada : Um nome de arquivo
# Saida : Um possivel arquivo
# Autora : Maria Emilia Bergo - mariaemilia.bergo@gmail.com (adaptado de f_Candido)

from socket import *
import sys
import os

#serverName = gethostname()
#serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

arg = raw_input('navegador ')

try:
	entrada = arg.split(' ')
	serverName = entrada[0]
	serverPort = int(entrada[1])
	# Conecta como cliente a um servidor selecionado utilizando a porta especificada 
	clientSocket.connect((serverName,serverPort))
	#s.connect((url, int(porta)))

except Exception as e:
	# Conecta como cliente a um servidor selecionado
	# utilizando a porta especificada 
	clientSocket.connect((serverName,80))
	#s.connect((arg,80))

clientSocket.connect((serverName,serverPort))

#print 'navegador ', serverName,'porta', serverPort

print '\033[32m'+'\nConexao extabelecida...'+'\033[0;0m'

arquivo = raw_input('Nome do arquivo: ')
caminho = raw_input('Diretorio: ')
requisicao = arquivo + ' ' + caminho

#requisicao = raw_input('Nome do arquivo: ')

clientSocket.send(requisicao)

resposta = clientSocket.recv(5120)

print '\033[32m'+'\nResultado da busca:'+'\033[0;0m'
print resposta

clientSocket.close()