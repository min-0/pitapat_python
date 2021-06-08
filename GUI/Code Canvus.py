from tkinter import Tk, Canvas

root = Tk()

def clicked(event):
    canvas.create_text(event.x, event.y, text='({},{})'.format(event.x , event.y))

canvas = Canvas(root, width  = 200, height = 100)
canvas.bind('<Button>', clicked)
canvas.pack()

root.mainloop()