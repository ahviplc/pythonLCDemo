import tkinter

'''
鼠标点击事件
'''
win = tkinter.Tk()
win.title("25_Mouse_Click_Demo.py By LC")
win.geometry("400x400+200+50")


def func(event):
    print(event.x, event.y)


# <Button-1>  鼠标左键
# <Button-2>  鼠标滚轮
# <Button-1>  鼠标右键
# <Double-Button-1>  鼠标双击左键
# <Triple-Button-1>  鼠标三击左键

button1 = tkinter.Button(win, text="leftmouse button")
# bind 给控件绑定数据（参数一是绑定的事件，参数二是触发事件的函数）
button1.bind("<Button-1>", func)
button1.pack()

win.mainloop()
