from tkinter import *

top = Tk()

cnvs = Canvas(top, width=300, height=200)
cnvs.pack()
cnvs.create_polygon(10, 10, 150, 110, 250, 20, fill='blue')
# x1, y1, x2, y2, x3, y3, color 점 세개면 삼각형, 점 네개면 사각형,,,

top.mainloop()
