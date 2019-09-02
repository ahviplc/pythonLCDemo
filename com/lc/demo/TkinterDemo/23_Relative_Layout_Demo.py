import tkinter

'''
相对布局
'''
win = tkinter.Tk()
win.title("23_Relative_Layout_Demo.py By LC")
win.geometry("400x400+200+50")

label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="red")
label3 = tkinter.Label(win, text="cool", bg="green")

# 相对布局，窗体改变对控件有影响
label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack()

win.mainloop()
