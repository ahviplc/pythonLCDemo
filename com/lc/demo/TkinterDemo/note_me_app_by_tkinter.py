# !/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
# from tkinter import *  # 导入 Tkinter 库
import tkinter
from tkinter import Frame, Text, Scrollbar, Pack, Grid, Place
from tkinter.constants import RIGHT, LEFT, Y, BOTH

# 用Tkinter编写交互日记系统

# 改变系统环境编码为简体中文utf-8-为了让oracle查询出的中文不乱码
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class ScrolledText(Text):
    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)

        kw.update({'yscrollcommand': self.vbar.set})
        Text.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)


def enter_and_print(event):
    print(var.get())
    text_output.delete(0.0, 'end')
    text_output.insert(0.0, var.get())
    var.set('')


root = tkinter.Tk()
root.title("Alan's diary")

var = tkinter.StringVar(value="What do you want to write today?")

text_input = tkinter.Entry(root, textvariable=var, width=36, bd=5)
text_input.pack()

root.bind('<Return>', enter_and_print)

text_output = ScrolledText(root, width=46)
text_output.pack()

root.mainloop()
