"""

套接字 - 基于UDP协议创建Echo客户端

Version: 0.1
Author: LC
DateTime:2018年11月14日16:31:12
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from socket import *

client = socket(AF_INET, SOCK_DGRAM)
while True:
	data_str = input('请输入: ')
	client.sendto(data_str.encode('utf-8'), ('localhost', 6789))
	data, addr = client.recvfrom(1024)
	data_str = data.decode('utf-8')
	print('服务器回应:', data_str)
	if data_str == 'bye':
		break
client.close()
