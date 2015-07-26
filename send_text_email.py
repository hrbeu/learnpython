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
