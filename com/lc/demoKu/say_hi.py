# coding=utf-8
import getopt
import sys

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'hn:w:', ['name=', 'word=', 'help'])

    name = 'No Name'
    word = 'Hello'
    for key, value in opts:

        if key in ['-h', '--help']:
            print('一个向人打招呼的程序')
            print('参数：')
            print('-h\t显示帮助')
            print('-n\t你的姓名')
            print('-w\t想要说的话')
            sys.exit(0)
        if key in ['-n', '--name']:
            name = value
        if key in ['-w', '--word']:
            word = value

    print('你好，我叫', name, '，', word)

    # 运行示例

    # $ python
    # say_hi.py
    # 你好，我叫
    # No
    # Name ， Hello
    #
    # $ python
    # say_hi.py - h
    # 一个向人打招呼的程序
    # 参数：
    # -h
    # 显示帮助
    # -n
    # 你的姓名
    # -w
    # 想要说的话
    #
    # $ python
    # say_hi.py - -help
    # 一个向人打招呼的程序
    # 参数：
    # -h
    # 显示帮助
    # -n
    # 你的姓名
    # -w
    # 想要说的话
    #
    # $ python
    # say_hi.py - n
    # 'ppppfly'
    # 你好，我叫
    # ppppfly ， Hello
    #
    # $ python
    # say_hi.py - n
    # 'ppppfly' - w
    # '我胡汉三又回来啦！'
    # 你好，我叫
    # ppppfly ， 我胡汉三又回来啦！
    #
    # $ python
    # say_hi.py - -name
    # 'ppppfly' - -word
    # '我胡汉三又回来啦！'
    # 你好，我叫
    # ppppfly ， 我胡汉三又回来啦！




#PS D:\all_develop_soft\pycharm-professional-2018.1.3\codeKu\pythonLCDemo\com\lc\demoKu> python .\say_hi.py
#你好，我叫 No Name ， Hello
#PS D:\all_develop_soft\pycharm-professional-2018.1.3\codeKu\pythonLCDemo\com\lc\demoKu> python .\say_hi.py -h
#一个向人打招呼的程序
# 参数：
# -h      显示帮助
# -n      你的姓名
# -w      想要说的话
#
#PS D:\all_develop_soft\pycharm-professional-2018.1.3\codeKu\pythonLCDemo\com\lc\demoKu> python .\say_hi.py -n LC -w woaini
#你好，我叫 LC ， woaini
#
#
#