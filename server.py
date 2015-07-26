#-*-coding:utf-8-*-
import socket
import threading
import time

class server(object):
	def __init__(self):
		self.ip='127.0.0.1'
		self.port=9999
	def serve(self):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
		s.bind((self.ip,self.port))
		s.listen(5)
		print 'Waiting for connection...'
		while 1:
			sock,addr=s.accept()
			t=threading.Thread(target=self.tcplink,args=(sock,addr))
			t.start()
	def tcplink(self,sock,addr):
		print 'Accept connection from %s:%s' % addr
		sock.send('Welcome')
		while 1:
			data=sock.recv(1024)
			time.sleep(1)
			if data=='exit' or not data:
				break
			sock.send('Hello %s' % data)
		sock.close()
		print 'Connection closed from %s:%s' % addr
if __name__=='__main__':
	server1=server()
	server1.serve()


'''
#-*- coding:utf-8 -*- 

import socket
 
HOST, PORT = '127.0.0.1', 8000
 
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    http_response="""
HTTP/1.1   200 OK

HELLO WORLD!
"""
    client_connection.sendall(http_response)
    client_connection.close()
'''
