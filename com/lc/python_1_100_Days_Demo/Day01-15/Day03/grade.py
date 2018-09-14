"""

百分制成绩转等级制成绩
90分以上 	 	--> A
80分~89分 	--> B
70分~79分	--> C
60分~69分	--> D
60分以下		--> E

Version: 0.1
Author: LC
DateTime:2018年9月14日17:17:07
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html

"""

score = float(input('请输入成绩: '))
if score >= 90:
	grade = 'A'
elif score >= 80:
	grade = 'B'
elif score >= 70:
	grade = 'C'
elif score >= 60:
	grade = 'D'
else:
	grade = 'E'
print('对应的等级是:', grade)
