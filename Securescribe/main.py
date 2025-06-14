import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()

with open('pass.txt','r') as f:
    password=f.read()
server.login('jsan33665@gmail.com', password)
msg=MIMEMultipart()
msg['From']='jananikumar'
msg['To']='jananikumarsan@gmail.com'
msg['Subject']='Just a Test'

with open('msg.txt','r') as f:
    message=f.read()

msg.attach(MIMEText(message, 'plain'))

filename='bubbles.jpg'
attachment=open(filename,'rb')

p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment; filename={filename}')

text=msg.as_string()
server.sendmail('jsan33665@gmail.com','jananikumarsan@gmail.com',text)
