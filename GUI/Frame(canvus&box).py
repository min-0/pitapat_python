from tkinter import *


def up():
    'move pen up 10 pixels'
    global y, canvas
    canvas.create_line(x, y, x, y-10)
    y -= 10


def down():
    'move pen down 10 pixels'
    global y, canvas
    canvas.create_line(x, y, x, y+10)
    y += 10


def left():
    'move pen left 10 pixels'
    global x, canvas
    canvas.create_line(x, y, x-10, y)
    x -= 10


def right():
    'move pen right 10 pixels'
    global x, canvas
    canvas.create_line(x, y, x+10, y)
    x += 10


root = Tk()

canvas = Canvas(root, width=150, height=100, relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

box = Frame(root)
box.pack(side=RIGHT)

b1 = Button(box, text='up', command=up)
b1.grid(row=0, column=0, columnspan=2)

b1 = Button(box, text='left', command=left)
b1.grid(row=1, column=0)

b1 = Button(box, text='right', command=right)
b1.grid(row=1, column=1)

b1 = Button(box, text='down', command=down)
b1.grid(row=2, column=0, columnspan=2)

x, y = 50, 75  # 펜 위치, 중앙으로 초기화

root.mainloop()
