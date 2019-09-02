import tkinter

'''
表格布局
'''
win = tkinter.Tk()
win.title("24_Table_Layout_Demo.py By LC")
win.geometry("400x400+200+50")

label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="red")
label3 = tkinter.Label(win, text="cool", bg="green")
label4 = tkinter.Label(win, text="handsome", bg="yellow")

# 表格布局
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

win.mainloop()
