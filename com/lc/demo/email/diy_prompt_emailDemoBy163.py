# -*- coding: utf-8 -*-

"""
diy_prompt_emailDemoBy163.py
结合命令窗口输入发送邮件示例
Version: 1.0
Author: LC
DateTime: 2019年1月10日11:02:28
UpdateTime: None
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "ahviplc@163.com"  # 用户名
mail_pass = "###"  # 口令


# 自定义输入方法
def prompt(prompt):
    sys.stdout.write(prompt + "->")
    sys.stdout.flush()
    return sys.stdin.readline().strip()


if __name__ == '__main__':

    sender = prompt("发送者-From")
    receivers = prompt("接收者-若多个接收者,请用 , 分隔-To").split(',')  # 若需要发送给多个人，请在每个邮箱后面使用 , 分隔即可！此会分隔成列表！
    print("按ctrl+D键结束输入发送内容-Enter message, end with ^D:")  # 这里是按ctrl+D键结束输入
    msg = ''
    while 1:
        line = sys.stdin.readline()
        if not line:
            break
        msg = msg + line
    print("Message length is %d" % len(msg))

    # 构造邮件对象MIMEText对象 MIMEText配置
    # 下面的主题， 发送者，接收者是显示在邮件页面上的。

    # 构造MIMEText对象时，第一个参数是邮件正文，第二个参数是MIME的subtype，最后一定要用utf-8  编码保证多语言兼容性。
    message = MIMEText(msg, 'plain', 'utf-8')
    # message = MIMEText('Python SMTP Test hello lc 1805302159', 'plain', 'utf-8')

    # message['From'] = "ahviplc@163.com"   # 发送者
    message['From'] = sender  # 发送者

    # message['To'] = "ahlc@sina.cn"  # receiver's name could be customized  # 接收者
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
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件" + str(e))
        smtpObj.quit()

# 执行demo输出样例1
# 发送者-From->ahviplc@163.com
# 接收者-若多个接收者,请用 , 分隔-To->ahlc@sina.cn,835661383@qq.com
# 按ctrl+D键结束输入发送内容-Enter message, end with ^D:    # 这里是按ctrl+D键结束输入
# 123木头人
# ^D
# Message length is 7
# 邮件发送成功

# 执行demo输出样例2
# 发送者-From->ahviplc@163.com
# 接收者-若多个接收者,请用 , 分隔-To->ahlc@sina.cn,835661383@qq.com,1464420980@qq.com
# 按ctrl+D键结束输入发送内容-Enter message, end with ^D:
# 321木头人
# ^D
# Message length is 7
# 邮件发送成功

# 执行demo输出样例3
# 发送者-From->ahviplc@163.com
# 接收者-若多个接收者,请用 , 分隔-To->ahlc@sina.cn
# 按ctrl+D键结束输入发送内容-Enter message, end with ^D:
# 123木头人 中文
# ^D
# Message length is 10
# 邮件发送成功

# 详细教程网址:
# python自动发邮件总结及实例说明 - 啄木鸟儿 - 博客园
# https://www.cnblogs.com/yufeihlf/p/5726619.html
