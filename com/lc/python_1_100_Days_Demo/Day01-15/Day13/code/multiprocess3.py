"""

创建进程调用其他程序

Version: 0.1
Author: LC
DateTime:2018年11月14日16:11:39
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html


"""

import subprocess
import sys

def main():
	# 通过sys.argv获取命令行参数
	if len(sys.argv) > 1:
		# 第一个命令行参数是程序本身所以从第二个开始取
		for index in range(1, len(sys.argv)):
			try:
				# 通过subprocess模块的call函数启动子进程
				status = subprocess.call(sys.argv[index])
			except FileNotFoundError:
				print('不能执行%s命令' % sys.argv[index])
	else:
		print('请使用命令行参数指定要执行的进程')


if __name__ == '__main__':
	main()
