"""

套接字 - 基于UDP协议Echo服务器

Version: 0.1
Author: LC
DateTime:2018年11月14日16:31:05
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from socket import *
from time import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 6789))
while True:
	data, addr = server.recvfrom(1024)
	server.sendto(data, addr)
server.close()
