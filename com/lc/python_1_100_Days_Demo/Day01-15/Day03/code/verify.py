"""

用户身份验证

Version: 0.1
Author: LC
DateTime:2018年9月14日17:20:36
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

# import getpass
# from getpass import getpass
# from getpass import *

username = input('请输入用户名: ')
password = input('请输入口令: ')
# 输入口令的时候终端中没有回显
# password = getpass.getpass('请输入口令: ')
if username == 'admin' and password == '123456':
	print('身份验证成功!')
else:
	print('身份验证失败!')
