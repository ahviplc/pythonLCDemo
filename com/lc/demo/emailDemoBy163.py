#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="ahviplc@163.com"    #用户名
mail_pass="###"   #口令

#
sender = 'ahviplc@163.com'
receivers = ['ahlc@sina.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python SMTP Test hello lc', 'plain', 'utf-8')
message['From'] = "ahviplc@163.com"
message['To'] =  "ahlc@sina.cn" # receiver's name could be customized

subject = 'Python SMTP Test LC title'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print ("Error: 无法发送邮件"+str(e))