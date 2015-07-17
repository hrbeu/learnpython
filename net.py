#!/usr/bin/env Python
#-*-coding:utf-8-*-
import time
import sys

if len(sys.argv)>1:
    INTERFACE=sys.argv[1]
else:
    INTERFACE='eth0'

STATS=[]

print 'Interface: ',INTERFACE

def rx():
    ifstat=open('/proc/net/dev').readlines()
    for interface in ifstat:
        if INTERFACE in interface:
            stat=float(interface.split()[1])
            STATS[0:]=[stat]
def tx():
    ifstat=open('/proc/net/dev').readlines()
    for interface in ifstat:
        if INTERFACE in interface:
            stat=float(interface.split()[9])
            STATS[1:]=[stat]

print ' IN     OUT'
rx()
tx()

while 1:
    time.sleep(1)
    rxstat_o=list(STATS)
    rx()
    tx()
    #print rxstat_o
    #print STATS
    RX_RATE=round((STATS[0]-rxstat_o[0])/1024/1024,3)
    TX_RATE=round((STATS[1]-rxstat_o[1])/1024/1024,3)
    print RX_RATE,'MB',TX_RATE,'MB'


