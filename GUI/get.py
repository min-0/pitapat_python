from tkinter import *
from typing import Counter
top = Tk()


def showName():
    print("User Name: ", en.get())


lb = Label(top, text="User Name").grid(row=0)
en = Entry(top)
en.grid(row=0, column=1)

bt1 = Button(top, text="show", command=showName)  # 이름 출력
bt2 = Button(top, text="Quit", command=top.quit)  # 프로그램 종료

bt1.grid(row=1, column=0)
bt2.grid(row=1, column=1)

top.mainloop()
