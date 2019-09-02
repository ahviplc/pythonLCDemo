#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

'''
Button：按钮控件
'''

def func():
    print("Hello TK,Hello LC!-button1")


win = tkinter.Tk()
win.title("3_Button_Demo.py By LC")
win.geometry("400x400+200+50")

# 创建按钮
button1 = tkinter.Button(win, text="按钮", command=func, width=10, height=10)
button1.pack()

button2 = tkinter.Button(win, text="按钮", command=lambda: print("Hello TK,Hello LC!-button2"))
button2.pack()

button3 = tkinter.Button(win, text="退出", command=win.quit)
button3.pack()

win.mainloop()
