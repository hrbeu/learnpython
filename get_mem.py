#/usr/bin/env Python
#-*-coding:utf-8-*-
from collections import OrderedDict

def meminfo():
    meminfo=OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0].strip()]=line.split(':')[1].strip()
    return meminfo

if __name__=="__main__":
    print 'Total memory:   ',meminfo()['MemTotal']
    print 'Free  memory:   ',meminfo()['MemFree']
