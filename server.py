#!/usr/bin/python
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = ("127.0.0.1",5555)
tcp.bind(orig)
tcp.listen(1)

while True:
    conn, cliente = tcp.accept()
    print 'Conectado por ', cliente
    while True:
        msg = conn.recv(1024)
        if not msg: break
        print cliente, msg
        conn.send("Recebido")
    print 'Finalizando conexao do cliente', cliente
    conn.close()