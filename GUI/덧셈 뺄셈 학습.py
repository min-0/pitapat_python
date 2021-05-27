from tkinter import *
import random
from tkinter.messagebox import showinfo

top = Tk()
top.title("덧셈 및 뺄셈 학습")


class Ed(Frame):
    def __init__(self, top):
        Frame.__init__(self, top)
        self.pack()
        self.calc = Entry(self)
        self.res = Entry(self)
        self.bt = Button(self, command=self.check, text="Enter", width=20)
        self.cnt = 0
        self.question()
        self.calc.pack(padx=100)
        self.res.pack(padx=100)
        self.bt.pack()
        self.Enter()

    def question(self):
        a = random.randrange(1, 10)
        b = random.randrange(1, 10)
        o = ['+', '-'].pop(random.randrange(0, 2))

        if o == '-' and a - b < 0:
            self.calc.insert(0, str(b) + o + str(a))
        else:
            self.calc.insert(0, str(a) + o + str(b))

    def check(self, event):
        self.cnt = self.cnt + 1
        result = eval(self.calc.get())
        if int(self.res.get()) == result:
            showinfo(message='Yot got it! ' + str(self.cnt) + "회 만에 성공")
            self.cnt = 0
            self.calc.delete(0, END)
            self.question()
        else:
            showinfo(message='Try again')
        self.res.delete(0, END)

    def Enter(self):
        self.res.bind("<Return>", self.check)


Ed(top).pack()

top.mainloop()
