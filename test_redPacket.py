#-*-coding:utf-8-*-

#使用python自带的unittest对进行redPacket.py单元测试
import redPacket
import random
import unittest

class TestRedPacket(unittest.TestCase):
    #按照模块约定的格式，把测试代码放在以test_开头的函数里，将会被自动进行测试
    def test_red(self):
        tests=100
        for i in range(tests):
            people=random.randint(1,20)
            money=random.randint(people,people*20000)
            result=redPacket.redPacket(people,money)
            print u'人数:',people,',',u'钱数:',money/100.0,u'(元)','->',u'分配方案',result
            #如果有红包金额小于1分钱则报错
            for r in result:
                self.assertGreaterEqual(r,0.01)
            #如果发出的红包的总金额与原定总钱数不符则报错
            total=0
            for r in result:
                total+=r
            self.assertAlmostEqual(total,money / 100.0)

if __name__=='__main__':
    unittest.main()





'''

#自己写的对红包程序redPacket.py的单元测试
import redPacket
import random

tests=100
for i in range(tests):
    people=random.randint(1,20)
    money=random.randint(people,people*20000)
    result=redPacket.redPacket(people,money)
    print u'人数:',people,',',u'钱数:',money/100.0,u'(元)','->',u'分配方案',result

#如果有红包金额小于1分钱则报错
for r in result:
    if r<0.01:
        print 'ERROR:result<0.01'

#如果发出的红包的总金额与原定总钱数不符则报错
#计算机中的小数是以二进制的科学计算法来存储，故一个小数的实际值与显示值有误差，所以不能用if total==money/100.0来判断
total=0
for r in result:
    total+=r
    if total-money / 100.0>0.00001:
        print 'ERROR:total result!=money'

'''