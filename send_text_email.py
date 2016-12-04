#-*-coding:utf-8-*-
#发送纯文本邮件

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((\
		Header(name,'utf-8').encode(),\
		addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr=raw_input('From:')
password=raw_input('Password:')
to_addr=raw_input('To:')
smtp_server=raw_input('SMTP SERVER:')

msg=MIMEText(u'用python发的第一封邮件，不知道能不能出去呀','plain','utf-8')
'''
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
'''
msg['From']=_format_addr(u'姜波 <%s>' % from_addr)
#msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可
msg['To']=_format_addr(u'二蛋子 <%s>' % to_addr)
#包含中文需要通过Header对象进行编码
msg['Subject']=Header(u'这是我用python发的邮件……','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)  # SMTP协议默认端口是25 
server.set_debuglevel(1)             #打印出和SMTP服务器交互的所有信息
server.login(from_addr,password)
#sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list
#邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
'''
import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.163.com'  
#163用户名
mail_user = '159*****02'  
#密码 
mail_pass = '7*passwd*x'   
#邮件发送方邮箱地址
sender = '159*****02@163.com'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['59*****02@qq.com']  

#设置email信息
#邮件内容设置
message = MIMEText('content','plain','utf-8')
#邮件主题       
message['Subject'] = 'title' 
#发送方信息
message['From'] = sender 
#接受方信息     
message['To'] = receivers[0]  

#登录并发送邮件
try:
    smtpObj = smtplib.SMTP() 
    #连接到服务器
    smtpObj.connect(mail_host,25)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass) 
    #发送
    smtpObj.sendmail(sender,receivers,message.as_string()) 
    #退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误   
'''
