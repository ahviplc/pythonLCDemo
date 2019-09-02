import tkinter

win = tkinter.Tk()
win.title("15_Spinbox_Demo.py By LC")
win.geometry("400x400+200+50")

'''
Spinbox控件
数值范围控件
'''

# 绑定变量
v = tkinter.StringVar()


def updata():
    print(v.get())


# increment：步长，默认为1
# values要输入一个元组 最好不要和from和to同时使用，而且步长也没用
# command 只要值改变就会执行updata方法
sp = tkinter.Spinbox(win, from_=0, to=100, increment=5,
                     textvariable=v, command=updata)
# sp = tkinter.Spinbox(win, values=(0,2,4,6,8))
sp.pack()

# 赋值
v.set(20)
# 取值
print(v.get())

win.mainloop()
