"""

套接字 - 基于TCP协议创建时间客户端

Version: 0.1
Author: LC
DateTime:2018年11月14日16:30:56
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 6789))
while True:
	data = client.recv(1024)
	if not data:
		break
	print(data.decode('utf-8'))
client.close()
