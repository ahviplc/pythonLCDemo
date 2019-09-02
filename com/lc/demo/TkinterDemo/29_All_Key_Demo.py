import tkinter

'''
响应所有按键的事件
'''
win = tkinter.Tk()
win.title("29_All_Key_Demo.py By LC")
win.geometry("400x400+200+50")

# <Key>  响应所有的按键（要有焦点）

label = tkinter.Label(win, text="*********", bg="red")
# 设置焦点
label.focus_set()
label.pack()


def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)


label.bind("<Key>", func)

win.mainloop()
