from tkinter import *


def record(event):
    print('char = {}'.format(event.keysym))


root = Tk()

text = Text(root, width=20, height=5)

text.bind("<KeyPress>", record)
text.pack(expand=True, fill=BOTH)

root.mainloop()
