import tkinter

"""
Radiobutton单选框
"""

win = tkinter.Tk()
win.title("9_Radiobutton_Demo.py By LC")
win.geometry("400x400+200+50")


def updata():
    print(r.get())


# 绑定变量，一组单选框要绑定同一个变量，就能区分出单选框了
r = tkinter.IntVar()

radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=updata)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=updata)
radio2.pack()

win.mainloop()
