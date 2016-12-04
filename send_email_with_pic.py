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
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#设置登录及服务器信息
mail_host = 'smtp.163.com'
mail_user = '159*****02'
mail_pass = '7******x'
sender = '159*****02@163.com'
receivers = ['7******0@qq.com']

#设置eamil信息
#添加一个MIMEmultipart类，处理正文及附件
message = MIMEMultipart()
message['From'] = sender
message['To'] = receivers[0]
message['Subject'] = 'title'
#推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
with open('abc.html','r') as f:
    content = f.read()
#设置html格式参数
part1 = MIMEText(content,'html','utf-8')
#添加一个txt文本附件
with open('abc.txt','r')as h:
    content2 = h.read()
#设置txt参数
part2 = MIMEText(content2,'plain','utf-8')
#附件设置内容类型，方便起见，设置为二进制流
part2['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
#添加照片附件
with open('1.png','rb')as fp:
    picture = MIMEImage(fp.read())
    #与txt文件设置相似
    picture['Content-Type'] = 'application/octet-stream'
    picture['Content-Disposition'] = 'attachment;filename="1.png"'
#将内容附加到邮件主体中
message.attach(part1)
message.attach(part2)
message.attach(picture)

#登录并发送
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('success')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print('error',e)
'''
