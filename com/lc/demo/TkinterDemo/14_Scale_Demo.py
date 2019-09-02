import tkinter

win = tkinter.Tk()
win.title("14_Scale_Demo.py By LC")
win.geometry("400x400+200+50")

'''
Scale控件
供用户通过拖拽指示器来改变变量的值，可以水平，也可以竖直
'''

# tkinter.HORIZONTAL水平
# tkinter.VERTICAL 竖直（默认）
# length:水平时表示宽度，竖直时表示高度
# tickintervar ：选择值将会为该值得倍数

scale1 = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=10, length=200)
scale1.pack()

# 设置值
scale1.set(20)


# 取值
# print(scale1.get())

def showNum():
    print(scale1.get())


tkinter.Button(win, text="按钮", command=showNum).pack()

win.mainloop()
