"""

Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: LC
DateTime:2018年9月18日11:11:32
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

from random import randint

money = 1000
while money > 0:
	print('你的总资产为:', money)
	needs_go_on = False
	while True:
		debt = int(input('请下注: '))
		if debt > 0 and debt <= money:
			break
	first = randint(1, 6) + randint(1, 6)
	print('玩家摇出了%d点' % first)
	if first == 7 or first == 11:
		print('玩家胜!')
		money += debt
	elif first == 2 or first == 3 or first == 12:
		print('庄家胜!')
		money -= debt
	else:
		needs_go_on = True

	while needs_go_on:
		current = randint(1, 6) + randint(1, 6)
		print('玩家摇出了%d点' % current)
		if current == 7:
			print('庄家胜')
			money -= debt
			needs_go_on = False
		elif current == first:
			print('玩家胜')
			money += debt
			needs_go_on = False

print('你破产了, 游戏结束!')
