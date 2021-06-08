from tkinter import *

top = Tk()

cnvs = Canvas(top, width=300, height=200)
cnvs.pack()
cnvs.create_text(100, 50, text='텍스트 (Text)')
cnvs.create_text(100, 100, text='X')

top.mainloop()
