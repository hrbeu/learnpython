#-*-coding:utf-8-*-
'''
囚徒问题：
在某个虚构的监狱里关押着n名囚犯，此监狱偶尔会有1个名额的假释机会，但决定名额的方式比较奇葩：
所有囚犯排成一个圈，以某个人为起点从1开始报数，依次递增。所有报到奇数的犯人立刻离开，剩下的人继续往下报数，最后剩下的一个犯人获得假释。
站在那个位置才能保证获得假释？实现一个函数lucky(n)让它返回幸运的数字。
'''


#方法一
def lucky(n):
    lst=range(1,n+1)
    count=0
    while len(lst)>1:
        #lst2=lst 并没有产生一个新列表，只是相当于给lst起了个别名lst2，所以对列表进行拷贝要用[:]
        lst2=lst[:]
        for i in lst:
            count+=1
            if count%2 !=0:
                lst2.remove(i)
        lst=lst2
    return lst[0]
n=input('number:')
print lucky(n)

'''
#方法二
def lucky(n):
    lst=range(1,n+1)
    #每次把队列中的第二个元素加到队尾，然后把前两个元素都删掉，一直循环直到剩下最后一个
    while len(lst)>1:
        lst.append(lst[1])
        del lst[0:2]
    return lst[0]
n=input('number:')
print lucky(n)
'''