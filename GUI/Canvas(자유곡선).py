from tkinter import *

top = Tk()

oldx, oldy = 0, 0


def begin(event):
    global oldx, oldy
    oldx, oldy = event.x, event.y


def draw(event):
    global oldx, oldy, cnvs
    newx, newy = event.x, event.y
    cnvs.create_line(oldx, oldy, newx, newy)  # 선 연결
    oldx, oldy = newx, newy


cnvs = Canvas(top, height=100, width=150)
cnvs.pack()

cnvs.bind('<Button-1>', begin)
cnvs.bind('<Button1-Motion>', draw)

top.mainloop()
