#-*-coding:utf-8-*-
from collections import OrderedDict

def CPUINFO():
#CPU_info like {'0':{'':'','':'',...},'1':{'':'','':'',...},...}
    CPU_info=OrderedDict()
    proc_info=OrderedDict()
    proc_id=0
    with open('/proc/cpuinfo') as f:
        for line in f:
#start of the info on one processor
            if line.strip():
                if line.split(':')[0] is not None and line.split(':')[1] is not None:
                    proc_info[line.split(':')[0].strip()]=line.split(':')[1].strip()
                else:
                    proc_info[line.split(':')[0].strip()]=''
#end of the info on one processor
            else:
                CPU_info[proc_id]=proc_info
                proc_id=proc_id+1
    return CPU_info

if __name__=="__main__":
    cpu_info=CPUINFO()
    for id in cpu_info.keys():
        print cpu_info[id]['model name']
