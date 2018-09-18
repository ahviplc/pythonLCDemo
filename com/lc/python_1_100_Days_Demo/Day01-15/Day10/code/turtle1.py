"""

用turtle模块绘图
这是一个非常有趣的模块 它模拟一只乌龟在窗口上爬行的方式来进行绘图

Version: 0.1
Author: LC
DateTime:2018年9月18日14:25:30
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
	turtle.forward(200)
	turtle.right(170)
turtle.end_fill()
turtle.mainloop()
