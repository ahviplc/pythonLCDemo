"""

使用socketserver模块创建时间服务器

Version: 0.1
Author: LC
DateTime:2018年11月14日16:31:19
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from socketserver import TCPServer, StreamRequestHandler
from time import *


class EchoRequestHandler(StreamRequestHandler):

	def handle(self):
		currtime = localtime(time())
		timestr = strftime('%Y-%m-%d %H:%M:%S', currtime)
		self.wfile.write(timestr.encode('utf-8'))


server = TCPServer(('localhost', 6789), EchoRequestHandler)
server.serve_forever()
