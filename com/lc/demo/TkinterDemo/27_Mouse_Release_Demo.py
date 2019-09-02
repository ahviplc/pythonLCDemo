import tkinter

'''
鼠标释放事件
'''
win = tkinter.Tk()
win.title("27_Mouse_Release_Demo.py By LC")
win.geometry("400x400+200+50")

# <ButtonRelease-1> 释放鼠标左键
# <ButtonRelease-2> 释放鼠标中键
# <ButtonRelease-3> 释放鼠标右键


label = tkinter.Label(win, text="*********", bg="red")
label.pack()


def func(event):
    print(event.x, event.y)


label.bind("<ButtonRelease-1>", func)

win.mainloop()
