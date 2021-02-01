# LC 2018年6月17日01:52:47
#
# python if __name__ == '__main__'
#
# 解析
# 废话不多说，正题：
#
# python中所有的模块都有一个内置属性
# __name__，一个模块的
# __name__
# 的值取决于如何应用模块。如果
# import 一个模块，那么模块__name__
# 的值通常为模块文件名，不带路径或者文件扩展名。但是您也可以像一个标准的程序样直接运行模块，在这
# 种情况下, __name__
# 的值将是一个特别缺省
# "__main__"。
#
#
#
# 换句通俗的话讲，当你在当前文件运行一个文件时，__name__ == __main__，则其后的代码会正常执行，但是当你在另一个文件import这个文件的时候，此时__name__！=__main__，则以下的代码将不会执行。至于他的作用，我简单的理解就是加入if
# __name__ == "__main__"
# 后，它后面的代码在其它地方引用时，就不执行，从而方便了代码的重用。示例：_name_And__main__description.py如下：

print('恋习Python')
print(__name__)


def main():
    print('恋习Python2 from main()')


# diy 方法
def diy_function():
    print('恋习diy_function')


if __name__ == '__main__':
    main()
    print('跟着菜鸟分析，练习Python越练越恋')

# D:\all_develop_soft\python-3.6.5-amd64-exe-ver\python.exe D:/all_develop_soft/pycharm-professional-2018.1.3/codeKu/pythonLCDemo/com/lc/demoKu/_name_And__main__description.py
# 恋习Python
# 恋习Python2 from main()
# 跟着菜鸟分析，练习Python越练越恋


# 当我在其它地方引用这个_name_And__main__description.py时，就不执行  main()

# 执行 _name_And__main__description_Test.py

# PS D:\all_develop_soft\pycharm-professional-2018.1.3\codeKu\pythonLCDemo\com\lc\demoKu> python .\_name_And__main__description_Test.py
# 恋习Python
# _name_And__main__description
# 恋习Python2 from main()
# 恋习diy_function

# 现在，我们在test.py脚本的if __name__=="__main__":之前加入print(__name__)，即将__name__打印出来，则最后运行结果如下：

# D:\all_develop_soft\python-3.6.5-amd64-exe-ver\python.exe D:/all_develop_soft/pycharm-professional-2018.1.3/codeKu/pythonLCDemo/com/lc/demoKu/_name_And__main__description.py
# 恋习Python
# __main__
# 恋习Python2 from main()
# 跟着菜鸟分析，练习Python越练越恋


# 可以看出，此时变量__name__的值为"__main__"。
#
# 再执行_name_And__main__description_Test.py，模块内容和执行结果如下：

# PS D:\all_develop_soft\pycharm-professional-2018.1.3\codeKu\pythonLCDemo\com\lc\demoKu> python _name_And__main__description_Test.py
# 恋习Python
# _name_And__main__description
# 恋习Python2 from main()
# 恋习diy_function


# 此时，_name_And__main__description_Test.py中的__name__变量值为_name_And__main__description，不满足__name__=="__main__"的条件，因此，无法执行其后的代码。


#
# 再仔细想想，其运行原理也就是：
#
# 由于每个python模块（python文件）都包含内置的变量__name__，当运行模块被执行的时候，__name__等于文件名（包含了后缀.py）。
# 如果import到其他模块中，则__name__等于模块名称（不包含后缀.py）。
# 而“__main__”等于当前执行文件的名称（包含了后缀.py）。所以当模块被直接执行时，__name__ == '__main__'结果为真；
# 而当模块被import到其他模块中时，__name__ == '__main__'结果为假，就是不调用对应的方法。
#
# 简而言之就是：__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。当模块被直接运行时，代码将被运行，
# 当模块是被导入时，代码不被运行。


# 浅入深谈：秒懂python编程中的if __name__ == 'main' 的作用和原理
# https://zhuanlan.zhihu.com/p/34112508
