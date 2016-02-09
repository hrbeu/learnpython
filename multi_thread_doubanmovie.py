#-*-coding:utf-8-*-
import urllib,time,thread

time_start=time.time()
data=[]

def get_content(i):
    id=1764796+i
    url='https://api.douban.com/v2/movie/subject/%d' % id
    d=urllib.urlopen(url).read()
    data.append(d)
    print i,time.time()-time_start
    print 'data:',len(data)

for i in range(30):
        print 'request movie:',i
        thread.start_new_thread(get_content,(i,))

raw_input('press ENTER to exit...\n')
