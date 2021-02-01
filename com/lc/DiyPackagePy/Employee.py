#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Python 面向对象 | 菜鸟教程
# https://www.runoob.com/python/python-object.html


# 员工类
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

# ...输出...
# Employee.__doc__: 所有员工的基类
# Employee.__name__: Employee
# Employee.__module__: DiyPackagePy.Employee
# Employee.__bases__: (<class 'object'>,)
# Employee.__dict__: {'__module__': 'DiyPackagePy.Employee', '__doc__': '所有员工的基类', 'empCount': 0, '__init__': <function Employee.__init__ at 0x000001D11BA110D0>, 'displayCount': <function Employee.displayCount at 0x000001D11BA11158>, 'displayEmployee': <function Employee.displayEmployee at 0x000001D11BA111E0>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>}

# 定义 IT 员工子类
class IT(Employee):  # 定义子类
    def __init__(self, skill):
        self.skill = skill  # 技能
        print('"调用子类构造方法 IT 创建子类对象"')
        # 父类
        Employee.empCount += 1

    def coding(self):
        print(self.name, ' 调用子类方法 IT 我我正在coding')


# 公共方法
def love_py():
    print("i love you py from Employee.py ... ")
