from initDemo import *

from initDemo.initTest2 import initTest2_printFuc  # 报错解决办法二,测试代码

import initDemo

"""
Python杂谈: __init__.py的作用以及实际练习
此次练习相关代码: initDemo包的所有文件 (com/lc/demo/initDemo) 和 initTestMain.py (com/lc/demo/initTestMain.py)
Version: 1.0
Author: LC
DateTime: 2019年1月3日15:45:57
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""

print('我在:com/lc/demo/initTestMain.py')

print('我在:com/lc/demo/initTestMain.py,时间:' + str(initDemo.time.time()))
# 只是import time 之后,import initDemo,未定义 __all__ = ['initTest','time'] ,这种写法 initDemo.time.time() 是支持的。

print('我在:com/lc/demo/initTestMain.py,时间2:' + str(time.time()))
# import time 之后,import initDemo,定义了 __all__ = ['initTest','time'] ,这种写法 time.time() 也是支持的。

initTest.initTest_printFuc()

# initTest2.initTest2_printFuc() # 报错解决办法一,测试代码

initTest2_printFuc()  # 报错解决办法二,测试代码

# -----------------------------------------------------------------------------------------------------------------------------------------------

# 执行:E:\pycharm-professional-2018.1.3\Code\pythonLCDemo\venv\Scripts\python.exe E:/pycharm-professional-2018.1.3/Code/pythonLCDemo/com/lc/demo/initTestMain.py
# 输出:

# 我在:initDemo/__init__.py
# 我在:com/lc/demo/initDemo/initTest.py
# 我在:com/lc/demo/initTestMain.py
# 我在:com/lc/demo/initTestMain.py,时间:1546503267.538993
# 我在:com/lc/demo/initTestMain.py,时间2:1546503459.8056352
# 函数initTest_printFuc:我在:com/lc/demo/initDemo/initTest.py

# -----------------------------------------------------------------------------------------------------------------------------------------------

# 再次测试:新增initTest2.initTest2_printFuc() 再次执行输出

# 报错如下:

# 在:initDemo/__init__.py
# Traceback (most recent call last):
# 我在:com/lc/demo/initDemo/initTest.py
# 我在:com/lc/demo/initTestMain.py
#   File "E:/pycharm-professional-2018.1.3/Code/pythonLCDemo/com/lc/demo/initTestMain.py", line 6, in <module>
# 函数:我在:com/lc/demo/initDemo/initTest.py
#    initTest2.initTest2_printFuc()
# NameError: name 'initTest2' is not defined

# -----------------------------------------------------------------------------------------------------------------------------------------------

# 报错解决办法一:
# 在initDemo/__init__.py修改代码为:

# __all__ = ['initTest','initTest2']
# print('我在:initDemo/__init__.py')

# 然后执行:initTest2.initTest2_printFuc()

# -----------------------------------------------------------------------------------------------------------------------------------------------

# 报错解决办法二:
# 在: com / lc / demo / initTestMain.py  新增代码:
# from initDemo.initTest2 import initTest2_printFuc
#
# 然后执行: initTest2_printFuc()

# -----------------------------------------------------------------------------------------------------------------------------------------------

# ღ( ´･ᴗ･` )比心-目前使用运行的是 报错解决办法二 方案

# 成功输出:

# 我在:initDemo/__init__.py
# 我在:com/lc/demo/initDemo/initTest.py
# 我在:com/lc/demo/initDemo/initTest2.py
# 我在:com/lc/demo/initTestMain.py
# 我在:com/lc/demo/initTestMain.py,时间:1546503267.538993
# 我在:com/lc/demo/initTestMain.py,时间2:1546503459.8056352
# 函数initTest_printFuc:我在:com/lc/demo/initDemo/initTest.py
# 函数initTest2_printFuc:我在:com/lc/demo/initDemo/initTest2.py

# -----------------------------------------------------------------------------------------------------------------------------------------------
# Python杂谈: __init__.py的作用 - TpCode - 博客园
# https://www.cnblogs.com/tp1226/p/8453854.html
#
# # 我们经常在python的模块目录中会看到 "__init__.py"  这个文件，那么它到底有什么作用呢？
# # Python模块包中__init__.py文件的作用总结:
#
# 1. 标识该目录是一个python的模块包（module package）
# 　  如果你是使用python的相关IDE来进行开发，那么如果目录中存在该文件，该目录就会被识别为 module package 。
#
# 2. 简化模块导入操作
#    2.1　实际上，如果目录中包含了 __init__.py 时，当用 import 导入该目录时，会执行 __init__.py 里面的代码。
#         -__init__.py 里面加一个print，如果执行了该文件就会输出。-print('我在:initDemo/__init__.py')-很显然，__init__.py 在包被导入时会被执行。
#    2.2  控制模块导入-from initDemo.initTest2 import initTest2_printFuc-在我们执行import时，当前目录是不会变的（就算是执行子目录的文件），还是需要完整的包名。
#            #2.2.1 栗子:通常__init__.py 文件为空，但是我们还可以为它增加其他的功能。我们在导入一个包时，实际上是导入了它的__init__.py文件。
#                   -这样我们可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入。
#            #
#            # # initDemo3
#            # # __init__.py
#            # import re
#            # import urllib
#            # import sys
#            # import os
#            #
#            # # initTest3.py
#            # import initDemo3
#            # print(initDemo3.re, initDemo3.urllib, initDemo3.sys, initDemo3.os)
#            # 注意这里访问__init__.py文件中的引用文件，需要加上包名。
#
#    2.3  偷懒的导入方法-from initDemo import * 和__all__ = ['initTest']一起使用。
#          -__init__.py中还有一个重要的变量，__all__, 它用来将模块全部导入。
#
# 3. 配置模块的初始化操作
# 　　在了解了 __init__.py 的工作原理后，应该能理解该文件__init__.py就是一个正常的python代码文件。
# 　　因此可以将初始化代码放入该文件中。
#
# Python __init__.py 作用详解 - Data&Truth - 博客园
# https://www.cnblogs.com/Lands-ljk/p/5880483.html
#
# 4：可以了解到，__init__.py主要控制包的导入行为。要想清楚理解__init__.py文件的作用，还需要详细了解一下import语句引用机制：
# 可以被import语句导入的对象是以下类型：
# 模块文件（.py文件）
# C或C++扩展（已编译为共享库或DLL文件）
# 包（包含多个模块）
# 内建模块（使用C编写并已链接到Python解释器中）
# 当导入模块时，解释器按照sys.path列表中的目录顺序来查找导入文件。
#
# 5:导入模块
# 模块通常为单独的.py文件，可以用import直接引用，可以作为模块的文件类型有.py、.pyo、.pyc、.pyd、.so、.dll
# 在导入模块时，解释器做以下工作：
# 已导入模块的名称创建新的命名空间，通过该命名空间就可以访问导入模块的属性和方法。
# 在新创建的命名空间中执行源代码文件。
# 创建一个名为源代码文件的对象，该对象引用模块的名字空间，这样就可以通过这个对象访问模块中的函数及变量
# import 语句可以在程序的任何位置使用，你可以在程序中多次导入同一个模块，但模块中的代码仅仅在该模块被首次导入时执行。后面的import语句只是简单的创建一个到模块名字空间的引用而已。
# sys.modules字典中保存着所有被导入模块的模块名到模块对象的映射。
#
# 6:导入包
# 多个相关联的模块组成一个包，以便于维护和使用，同时能有限的避免命名空间的冲突.
# 使用from语句可以把模块直接导入当前命名空间，from语句并不引用导入对象的命名空间，而是将被导入对象直接引入当前命名空间。
#
# 7:其他杂谈：
# 关于.pyc 文件 与 .pyo 文件
# .py文件的汇编,只有在import语句执行时进行，当.py文件第一次被导入时，它会被汇编为字节代码，并将字节码写入同名的.pyc文件中。
# 后来每次导入操作都会直接执行.pyc 文件（当.py文件的修改时间发生改变，这样会生成新的.pyc文件），
# 在解释器使用-O选项时，将使用同名的.pyo文件，这个文件去掉了断言（assert）、断行号以及其他调试信息，体积更小，运行更快。
# （使用-OO选项，生成的.pyo文件会忽略文档信息）
# -----------------------------------------------------------------------------------------------------------------------------------------------
