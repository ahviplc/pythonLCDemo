import tkinter

"""
Menu顶层菜单
"""
win = tkinter.Tk()
win.title("16_Menu_Demo.py By LC")
win.geometry("400x400+200+50")

# 菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)


def func():
    print("**********")


# 创建一个菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)

# 给菜单选项添加内容
for item in ['python', 'c', 'java', 'c++', 'c#', 'php', 'B', '退出']:
    if item == '退出':
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=func)

# 向菜单条上添加菜单选项
menubar.add_cascade(label='语言', menu=menu1)

win.mainloop()
