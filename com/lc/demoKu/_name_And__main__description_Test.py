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
