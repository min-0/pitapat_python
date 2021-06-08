from tkinter import *


class Draw(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        self.old, self.oldy = 0, 0

        self.cnvs = Canvas(self, height=100, width=150)

        self.cnvs.bind('<Button-1>', self.begin)
        self.cnvs.bind('<Button1-Motion>', self.draw)
        self.cnvs.pack(expand=True, fill=BOTH)

    def begin(self, event):
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        newx, newy = event.x, event.y
        self.cnvs.create_line(self.oldx, self.oldy, newx, newy)  # 선 연결
        self.oldx, self.oldy = newx, newy


top = Tk()
draw = Draw(top)
draw.pack()
top.mainloop()
