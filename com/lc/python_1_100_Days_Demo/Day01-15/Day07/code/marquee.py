"""

输入学生考试成绩计算平均分

Version: 0.1
Author: LC
DateTime:2018年9月18日11:45:35
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import os
import time


def main():
	str = 'Welcome to 1000 Phone Chengdu Campus      '
	while True:
		print(str)
		time.sleep(0.2)
		str = str[1:] + str[0:1]
		# for Windows use os.system('cls') instead
		os.system('clear')


if __name__ == '__main__':
	main()
