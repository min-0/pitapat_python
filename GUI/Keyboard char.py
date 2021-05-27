from tkinter import *


def Key(event):
    print(event.char, "가 입력됨.")


top = Tk()

text = Text(top, width=20, height=5)
text.pack()

text.bind('<Key>', Key)

top.mainloop()
