"""

猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: LC
DateTime:2018年9月18日11:11:58
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
	counter += 1
	number = int(input('请输入: '))
	if number < answer:
		print('大一点')
	elif number > answer:
		print('小一点')
	else:
		print('恭喜你猜对了!')
		break
print('你总共猜了%d次' % counter)
if counter > 7:
	print('你的智商余额明显不足')
