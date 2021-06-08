from tkinter import *
from random import *
import time

top = Tk()

cnvs = Canvas(top, width=300, height=200)
cnvs.pack()

ball = cnvs.create_oval(140, 90, 160, 110, fill="blue")

for i in range(100):
    x = randint(-10, 10)
    y = randint(-10, 10)
    cnvs.move(ball, x, y)
    top.update()
    time.sleep(0.1)

top.mainloop()
