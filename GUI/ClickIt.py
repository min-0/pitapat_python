from tkinter import *
from time import localtime, strftime
from tkinter.messagebox import showinfo

# 더 큰 윈도우에서 실행


class ClickIt(Frame):
    'GUI that shows current time'

    def __init__(self, master=None):
        'constructor'
        Frame.__init__(self, master=None)
        self.pack()
        button = Button(self, text='Click it', command=self.clicked)
        button.pack()

    def clicked(self):
        'prints day and time info'
        time = strftime('Day: %D %b %Y\n Time: %H:%M:%S %p', localtime())
        showinfo(message=time)


top = Tk()

root = Tk()
app = ClickIt(root)
app.pack()

root.mainloop()
