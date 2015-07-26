#-*-coding:utf-8-*-
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.connect(('127.0.0.1',9999))
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
	s.send(data)
	print s.recv(1024)
s.send('exit')
s.close()