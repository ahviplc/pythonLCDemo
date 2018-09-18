"""

从文本文件中读取数据

Version: 0.1
Author: LC
DateTime:2018年9月18日15:11:11
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import time


def main():
	# 一次性读取整个文件内容
	with open('致橡树.txt', 'r', encoding='utf-8') as f:
		print(f.read())

	# 通过for-in循环逐行读取
	with open('致橡树.txt', mode='r',encoding='utf-8') as f:
		for line in f:
			print(line, end='')
			time.sleep(0.5)
	print()

	# 读取文件按行读取到列表中
	with open('致橡树.txt',encoding='utf-8') as f:
		lines = f.readlines()
	print(lines)
	

if __name__ == '__main__':
	main()
