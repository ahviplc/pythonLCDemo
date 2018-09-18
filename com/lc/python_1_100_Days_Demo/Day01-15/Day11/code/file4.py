"""

读写二进制文件

Version: 0.1
Author: LC
DateTime:2018年9月18日15:18:42
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import base64

with open('mm.jpg', 'rb') as f:
	data = f.read()
	# print(type(data))
	# print(data)
	print('字节数:', len(data))
	# 将图片处理成BASE-64编码
	print(base64.b64encode(data))

with open('girl2.jpg', 'wb') as f:
	f.write(data)
print('写入完成!')
