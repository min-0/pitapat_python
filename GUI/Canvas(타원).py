from tkinter import *

top = Tk()

cnvs = Canvas(top, width=300, height=200)
cnvs.pack()
cnvs.create_rectangle(10, 10, 200, 150)  # x좌표, y좌표, 가로, 세로
# create_rectangle은 사각형

top.mainloop()
