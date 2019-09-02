#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter

"""
Checkbutton多选框控件
"""
win = tkinter.Tk()
win.title("8_Checkbutton_Demo.py By LC")
win.geometry("400x400+200+50")


def updata():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"

    # 清空text中所有内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)


# 要绑定的变量
hobby1 = tkinter.BooleanVar()
# 多选框
check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=updata)
check1.pack()
hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="power", variable=hobby2, command=updata)
check2.pack()
hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="people", variable=hobby3, command=updata)
check3.pack()

text = tkinter.Text(win, width=50, height=5)
text.pack()

win.mainloop()
