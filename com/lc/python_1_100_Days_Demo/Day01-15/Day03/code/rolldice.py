"""

掷骰子决定做什么事情

Version: 0.1
Author: LC
DateTime:2018年9月14日17:18:00
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from random import randint

face = randint(1, 6)
if face == 1:
	result = '唱首歌'
elif face == 2:
	result = '跳个舞'
elif face == 3:
	result = '学狗叫'
elif face == 4:
	result = '做俯卧撑'
elif face == 5:
	result = '念绕口令'
else:
	result = '讲冷笑话'
print(result)
