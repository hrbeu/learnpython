#-*-coding:utf-8-*-

import random

def redPacket(people,money):
    result=[]
    #需要发送的红包数
    remain=people
    #每个红包的最大额度为平均值的2倍
    max_money=money/people*2
    #发放红包，用分为单位计算金额
    for i in range(people):
        remain-=1
        #如果不是最后一个红包，则随机分配金额，为剩下的每个人预留出至少1分钱
        if remain>0:
            m=random.randint(1,min(money-remain,max_money))
        #如果是最后一个红包，则把剩下的钱全发送出去
        else:
            m=money
        money-=m
        #加入结果中用元为单位，所以除以100
        result.append(m/100.0)
    #返回红包结果
    return result

people=int(input('红包个数:\n'))
money=int(input('总金额:\n')*100)
result=redPacket(people,money)
print result
