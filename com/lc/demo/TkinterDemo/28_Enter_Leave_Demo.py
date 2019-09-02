import tkinter

win = tkinter.Tk()
win.title("28_Enter_Leave_Demo.py By LC")
win.geometry("400x400+200+50")

# <Enter>  当鼠标进入控件时触发事件
# <Leave>  当鼠标离开控件时触发事件

label = tkinter.Label(win, text="*********", bg="red")
label.pack()


def func(event):
    print(event.x, event.y)


label.bind("<Enter>", func)
label.bind("<Leave>", func)

win.mainloop()
