#-*-coding:utf-8-*
#发送带图片的邮件

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
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
smtp_server=raw_input('SMTP Server:')

msg=MIMEMultipart()
msg['From']=_format_addr(u'python爱好者<%s>' % from_addr)
msg['To']=_format_addr(u'管理员<%s>' % to_addr)
msg['Subject']=Header(u'来自SMTP的问候……','utf-8').encode()
#add MIMEText
msg.attach(MIMEText('send with file','plain','utf-8'))
'''
#把图片邮件正文
msg.attach(MIMEText('<html><body><h1>Hello</h1>'+
	'<p><img src='cid:0'></p>'+
	'</body></html>','html','utf-8'))
'''
#add file
with open('C:/users/lenovo/desktop/BingWallpaper-2015-07-08.jpg','rb') as f:
	# 设置附件的MIME和文件名，这里是png类型
	mime=MIMEBase('image','jpg',filename='BingWallpaper-2015-07-08.jpg')
	# 加上必要的头信息
	mime.add_header('Content-Disposition','attachment',filename='BingWallpaper-2015-07-08.jpg')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id', '0')
	# 把附件的内容读进来
	mime.set_payload(f.read())
	# 用Base64编码
	encoders.encode_base64(mime)
	# 添加到MIMEMultipart
	msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()