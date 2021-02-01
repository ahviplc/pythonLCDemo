import _name_And__main__description

_name_And__main__description.main()
_name_And__main__description.diy_function()

import os
import sys

# Python os.path() 模块 | 菜鸟教程
# https://www.runoob.com/python/python-os-path.html

# os.getcwd: 返回当前工作目录
print(os.getcwd())
# C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc\demoKu

# 当前文件路径
# os.path.realpath： 返回path的真实路径
print(os.path.realpath(__file__))
# C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc\demoKu\_name_And__main__description_Test.py

# 当前文件所在的目录，即父路径
# os.path.dirname：去掉文件名，单独返回目录路径 返回文件路径
# os.path.abspath: 返回绝对路径
# os.path.realpath： 返回path的真实路径
# os.path.split: 把路径分割成 dirname 和 basename，返回一个元组
print(os.path.abspath('.'))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.split(os.path.realpath(__file__)))
print(os.path.split(os.path.realpath(__file__))[0])
print(os.path.split(os.path.realpath(__file__))[1])
# C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc\demoKu
# C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc\demoKu
# ('C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo\\com\\lc\\demoKu', '_name_And__main__description_Test.py')
# C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc\demoKu
# _name_And__main__description_Test.py

# 拼接路径 拼接_name_And__main__description_Test2.py文件的
# os.path.join(path1[, path2[, ...]]): 把目录和文件名合成一个路径
print(os.path.join(os.path.abspath('.'), '_name_And__main__description_Test2.py'))
# C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc\demoKu\_name_And__main__description_Test2.py

# 获取当前工作的父目录 ！注意是父目录路径
# os.path.abspath(__file__) 作用： 获取当前脚本的完整路径
print(os.path.abspath('..'))
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc
# C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc

# os.path.basename: 用法是去掉目录路径，单独返回文件名 返回文件名
print(os.path.basename(os.path.realpath(__file__)))
# _name_And__main__description_Test.py

# 打印 print(sys.path)
# 其是python的搜索模块的路径集
print(sys.path)

# 将os.path.abspath('..')加入系统路径
sys.path.append(os.path.abspath('..'))

# 再次打印 print(sys.path)
print(sys.path)
# 即可看到 'C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo\\com\\lc' 加入了系统路径

print("------------------------------------------------------------------------------------------------")
# 接着使用 【'C:\\_developSoftKu\\PyCharm 2019.1.3\\#CodeKu\\pythonLCDemo\\com\\lc'】路径下 自定义包模块 DiyPackagePy
# com/lc/DiyPackagePy

import DiyPackagePy  # import 就会打印 【hi DiyPackagePy from __init__.py】

from DiyPackagePy.Employee import Employee, IT, love_py as lp_pro

lp_pro()  # i love you py from Employee.py ...

DiyPackagePy.hi()

DiyPackagePy.print_line()

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)

"创建 Employee 类的第三个对象"
import DiyPackagePy.Employee as Emp

Emp.love_py()  # i love you py from Employee.py ...

emp3 = Emp.Employee("Jane", 6000)

# 执行类的自带方法
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print("Total Employee %d" % Employee.empCount)

DiyPackagePy.print_line()

"创建 Employee 类的 子类 IT 对象"
it = Emp.IT("Python,Go")
it.name = 'ahviplc'
it.salary = '30000'
print("it -> ", it.name, it.salary, it.skill)
it.displayEmployee()
it.coding()

DiyPackagePy.print_line()

it1 = IT("Java")
it1.name = 'LC'
it1.salary = '26000'
print("it1 -> ", it1.name, it1.salary, it1.skill)
print("Total Employee %d" % Employee.empCount)
it1.coding()
# 调用父类方法
it1.displayEmployee()
it1.displayCount()

DiyPackagePy.print_line()
# 引入并使用类中公共方法
from DiyPackagePy.Employee import love_py

love_py()  # i love you py from Employee.py ...

from DiyPackagePy.Employee import love_py as lp

lp()  # i love you py from Employee.py ...

DiyPackagePy.print_line()

import DiyPackagePy.util

# 引入并使用工具类中的方法
import DiyPackagePy.util.get_util_info as gui

gui.get_util_info()

from DiyPackagePy.util.get_util_info import get_util_info

get_util_info()

from DiyPackagePy.util.get_util_info import get_util_info as gui2

gui2()

DiyPackagePy.print_line()

from DiyPackagePy.util.get_now_time import get_now_time as gnt

now_time_str = gnt()
print(now_time_str)

DiyPackagePy.print_line()

# import说明:
# python import模块时， 是在sys.path里按顺序查找的。
# sys.path是一个列表，里面以字符串的形式存储了许多路径。
# 使用A.py文件中的函数需要先将他的文件路径放到sys.path中

# 其他
# PS D:\all_develop_soft\pycharm-professional-2018.1.3\codeKu\pythonLCDemo\com\lc\demoKu> python .\_name_And__main__description_Test.py
# 恋习Python

# ...输出...
# 恋习Python
# _name_And__main__description
# 恋习Python2 from main()
# 恋习diy_function
