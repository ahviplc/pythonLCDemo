"""

读取CSV文件

Version: 0.1
Author: LC
DateTime:2018年9月18日15:03:26
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import csv

filename = 'example.csv'

try:
	with open(filename) as f:
		reader = csv.reader(f)
		data = list(reader)
except FileNotFoundError:
	print('无法打开文件:', filename)
else:
	for item in data:
		print('%-30s%-20s%-10s' % (item[0], item[1], item[2]))
