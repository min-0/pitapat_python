from tkinter import *

top = Tk()

cnvs = Canvas(top, width=300, height=200)
cnvs.pack()
img = PhotoImage(file='rock.png')
cnvs.create_image(100, 100, anchor=NW, image=img)
cnvs.create_image(100, 100, image=img)

top.mainloop()
