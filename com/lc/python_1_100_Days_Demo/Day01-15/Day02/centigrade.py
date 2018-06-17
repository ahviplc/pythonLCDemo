"""

将华氏温度转换为摄氏温度
F = 1.8C + 32


Version: 0.1
Author: LC
DateTime: 2018年6月17日21:54:15
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html



"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
