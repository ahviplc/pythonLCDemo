#!/usr/bin/python3

"""
emailDemoBy163.py
基于163邮箱的邮件发送demo
Version: 1.0
Author: LC
DateTime:2019年1月10日12:44:51
UpdateTime: 2019年1月10日12:44:55
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "ahviplc@163.com"  # 用户名
mail_pass = "###"  # 口令

#
sender = 'ahviplc@163.com'
receivers = ['ahlc@sina.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 构造邮件对象MIMEText对象 MIMEText配置
# 下面的主题， 发送者，接收者是显示在邮件页面上的

# 构造MIMEText对象时，第一个参数是邮件正文，第二个参数是MIME的subtype，最后一定要用utf-8  编码保证多语言兼容性。
message = MIMEText('Python SMTP Test hello lc 1805302159', 'plain', 'utf-8')

# message['From'] = "ahviplc@163.com"
# message['To'] =  "ahlc@sina.cn" # receiver's name could be customized
message['From'] = sender  # 发送者
message['To'] = ';'.join(receivers)  # 接收者  # 收件人为多个收件人,通过join将列表转换为以 ; 为间隔的字符串

# 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
# subject = '中文标题'
# subject = Header(subject, 'utf-8')
subject = 'Python SMTP Test LC title 中文'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    # smtpObj.set_debuglevel(1)  # 设置输出debug调试信息，默认不输出
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件" + str(e))
    smtpObj.quit()
