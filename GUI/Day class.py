from tkinter import *
from time import strptime, strftime, localtime
from tkinter.messagebox import showinfo

from ClickIt import *


class Day(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        # label
        label = Label(self, text="Enter date")
        label.grid(row=0, column=0)

        # entry
        self.dateEnt = Entry(self)
        self.dateEnt.grid(row=0, column=1)

        # button
        button = Button(self, text='Enter', command=self.compute)
        button.grid(row=1, column=0, columnspan=2)

    def compute(self):
        date = self.dateEnt.get()  # 엔트리 내의 문자열 반환
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))
        showinfo(message='{} was a {}'.format(date, weekday))
        self.dateEnt.delete(0, END)


root = Tk()

day = Day(root)
app = ClickIt(root)
day.pack()
app.pack()
root.mainloop()
