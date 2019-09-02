import tkinter

'''
Listbox控件四
列表框控件：可以包含一个或多个文本框
作用：在listbox控件的小窗口显示一个字符串
'''
win = tkinter.Tk()
win.title("13_Listbox_Demo_4.py By LC")
win.geometry("400x400+200+50")

# MULTIPLE支持多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()

for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)

win.mainloop()
