#!/usr/bin/python
__author__ = 'daniel.melo'
import socket

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5555            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print 'Para sair use CTRL+X\n'

msg = raw_input()
while msg <> '\x18':
    tcp.send(msg)
    data = tcp.recv(4096)
    print "Resposta:" + str(data)
    msg = raw_input()


tcp.close()