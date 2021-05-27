from tkinter import *


def calc(event):
    lb.configure(text="결과: " + str(eval(ent.get())))


top = Tk()

Label(top, text="파이썬 수식 입력").pack()

ent = Entry(top)
ent.bind("<Return>", calc)  # Enter Key를 눌렀을 때 실행
ent.pack()

lb = Label(top, text="결과: ")
lb.pack()

top.mainloop()
