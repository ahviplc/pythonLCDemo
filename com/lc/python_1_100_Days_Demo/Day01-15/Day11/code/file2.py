"""

读取圆周率文件判断其中是否包含自己的生日

Version: 0.1
Author: LC
DateTime:2018年9月18日15:13:15
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

birth = input('请输入你的生日: ')
with open('pi_million_digits.txt') as f:
	lines = f.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.strip()
	if birth in pi_string:
		print('Bingo!!!')
	else:
		print("貌似没有啊！！！")
