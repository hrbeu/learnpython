#_*_ coding:utf-8 _*_
import socket
import os
import ctypes
#对经过网卡的数据捕包
#host to listen
HOST='192.168.1.103'

def sniffing(host,win,socket_prot):
	while 1:
		sniffer=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
		sniffer.bind((HOST,0))
#include the IP headers in the caputured packets
		sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
		if win == 1:
			sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
#read in a single packet
		print sniffer.recvfrom(65565)

def main(host):
	if os.name=='nt':
		sniffing(host,1,socket.IPPROTO_IP)
	else:
		sniffing(host,0,socket.IPPROTO_ICMP)

if __name__=="__main__":
	main(HOST)



