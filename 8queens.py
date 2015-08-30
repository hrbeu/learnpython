#-*-coding:utf-8-*-

import random
import sys
#state[0]值为第一个皇后位置，以此类推
state=()
#判断是否与已有皇后冲突
def conflict(state,nextX):
        nextY=len(state)
        for i in range(nextY):
                if abs(nextX-state[i])==0 or abs(nextX-state[i])==nextY-i:
                #if abs(nextX-state[i]) in (0,nextY-i)
                        return True
        return False
#num是皇后总数也是棋盘行/列数,state是存放前面皇后位置信息的元组


def queen(num=8,state=()):
        #如果摆放的是最后一个皇后，只需要找出它的位置
        if len(state)==num-1:
                for pos in range(num):
                        if not conflict(state,pos):
                                yield (pos,)
        #如果摆放的不是最后一个皇后，则进行递归，假定后面排列的皇后都是正确的
        else:
                for pos in range(num):
                        if not conflict(state,pos):
                                for result in queen(num,state+(pos,)):
                                        yield (pos,)+result


'''
def queen(num=8,state=()):
        for pos in range(num):
                if not conflict(state,pos):
                        if len(state)==num-1:
                                yield (pos,)
                        else:
                                for result in queen(num,state+(pos,)):
                                        yield (pos,)+result
'''
'''
#用list代替生成器的函数实现
def queen(num=8,state=()):
        l=[]
        for pos in range(num):
                if not conflict(state,pos):
                        if len(state)==num-1:
                                 l.append((pos,))
                        else:
                                for result in queen(num,state+(pos,)):
                                        l.append((pos,)+result)
        return l
'''

#图形化显示解决方案
def prettyprint(solution):
        for pos in solution:
                print '. '*pos+'Q'+' .'*(len(solution)-pos-1)

if __name__=='__main__':
        try:
                if len(sys.argv)>1:
                        x=int(sys.argv[1])
                        prettyprint(random.choice(list(queen(num=x))))
                else:
                        prettyprint(random.choice(list(queen())))
        except IndexError:
                print 'NO SOLUTIONS'
  
