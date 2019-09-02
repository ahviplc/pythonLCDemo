import tkinter

'''
响应特殊按键事件
'''
win = tkinter.Tk()
win.title("30_Special_Key_Demo.py By LC")
win.geometry("400x400+200+50")

# <Shift_L>  只响应左侧的shift键
# <Shift_R>
# <F5>
# <Return>  也就是回车键
# <BackSpace>  返回,也就是退格键

label = tkinter.Label(win, text="*********", bg="red")
# 设置焦点
label.focus_set()
label.pack()


def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)


label.bind("<Shift_L>", func)

win.mainloop()
