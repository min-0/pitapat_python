from tkinter import *

top = Tk()
top.title("엔트리")

lb = Label(top, text="User Name").pack(side=LEFT)
ent = Entry(top, show='*').pack(side=RIGHT)  # show = 입력내용 숨기기

top.mainloop()
