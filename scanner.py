#-*-coding:utf-8-*-
import socket
import struct
import ctypes
import os
import threading
import time
from netaddr import IPNetwork,IPAddress
#使用udp对局域网内主机进行搜索

#Host to listen on
HOST='192.168.1.103'
#subnet to target
SUBNET='192.168.1.0/24'
#string signature
MESSAGE='hellooooo'
class ICMP(ctypes.Structure):
        _fields_=[
        ('type',ctypes.c_ubyte),
        ('code',ctypes.c_ubyte),
        ('checksun',ctypes.c_ushort),
        ('unused',ctypes.c_ushort),
        ('next_hop_mtu',ctypes.c_ushort)
        ]
        def __new__(self,socket_buffer):
                return self.from_buffer_copy(socket_buffer)
        def __init__(self,socket_buffer):
                pass
#sprays out udp datagrams
def udp_sender(SUBNET,MESSAGE):
        time.sleep(5)
        send_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
        for ip_addr in IPNetwork(SUBNET):
                try:
                        send_socket.sendto(MESSAGE,('%s'%ip_addr,65212))
                except:
                        pass


def main():
        t=threading.Thread(target=udp_sender,args=(SUBNET,MESSAGE))
        t.start()

        sniffer=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
        sniffer.bind((HOST,0))
        sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
        #continually read in packets and parse their information
        while 1:
                raw_buffer=sniffer.recvfrom(65565)[0]
                #print raw_buffer
                ip_header=raw_buffer[0:20]
                #print ip_header
                iph=struct.unpack('!BBHHHBBH4s4s',ip_header)
                #print iph
                #Create our IP struture
                version_ihl=iph[0]
                version=version_ihl>>4
                ihl=version_ihl&0xF
                iph_length=ihl*4
                ttl=iph[5]
                protocol=iph[6]
                s_addr=socket.inet_ntoa(iph[8])
                d_addr=socket.inet_ntoa(iph[9])
               # print 'IP VERSION: '+str(version)+',HEADER LENGTH: '+str(ihl)+',TTL: '+str(ttl)+',PROTOCOL: '+str(protocol)+',SOURCE ADDRESS: '+str(s_addr)+',DESTINATION ADDRESS: '+str(d_addr)
                #create our icmp stucture
                icmp_buffer=raw_buffer[iph_length:iph_length+ctypes.sizeof(ICMP)]
                icmp_header=ICMP(icmp_buffer)
               # print 'ICMP CODE: '+str(icmp_header.code)+',ICMP TYPE: '+str(icmp_header.type)+'\n'
                #check for the type and the code within the subnet
                if icmp_header.type==3 and icmp_header.code==3:
                        if IPAddress(s_addr) in IPNetwork(SUBNET):
                                if raw_buffer[len(raw_buffer)-len(MESSAGE):]==MESSAGE:
                                        print ('Host up: %s' % s_addr)



if __name__=='__main__':
        main()
