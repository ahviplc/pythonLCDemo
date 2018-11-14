"""

套接字 - 基于TCP协议创建时间服务器

Version: 0.1
Author: LC
DateTime:2018年11月14日16:30:33
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from socket import *
from time import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 6789))
server.listen()
print('服务器已经启动正在监听客户端连接.')
while True:
	client, addr = server.accept()
	print('客户端%s:%d连接成功.' % (addr[0], addr[1]))
	currtime = localtime(time())
	timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
	client.send(timestr.encode('utf-8'))
	client.close()
server.close()
