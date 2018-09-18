"""

英制单位英寸和公制单位厘米互换

Version: 0.1
Author: LC
DateTime:2018年9月14日17:16:50
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
	print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
	print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
	print('请输入有效的单位')
