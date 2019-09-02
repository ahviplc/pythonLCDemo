#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("4_Entry_Demo.py By LC")
win.geometry("400x400+200+50")

'''
Entry：输入控件，用于显示简单的文本内容
'''

# 密文显示
# 绑定变量
e1 = tkinter.Variable()
entry1 = tkinter.Entry(win, show="*", textvariable=e1)  # show="*" 可以表示输入密码

entry1.pack()

# 绑定变量
e2 = tkinter.Variable()

entry2 = tkinter.Entry(win, textvariable=e2)
entry2.pack()

# e就代表输入框这个对象
# 设置值
e2.set("ahviplc")
# 取值
print(e2.get())
print(entry2.get())

e1.set("ahviplc_pass")
print(entry1.get())
print(e1.get())

win.mainloop()
