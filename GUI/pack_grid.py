from tkinter import *

w = Tk()
bt0 = Button(w, text='c0', width=10, height=3)
Button(w, text='r0, c1', width=10).grid(row=0, column=1)
Button(w, text='r1, c1', width=10).grid(row=1, column=1)
Button(w, text='r2, c0', width=10).grid(row=2, column=0)
Button(w, text='r2, c1', width=10).grid(row=2, column=1)
bt0.grid(row=0, column=0, rowspan=2)  # rowspan

bt1 = Button(w, text='r3', width=20)
Button(w, text='r4, c0', width=10).grid(row=4, column=0)
Button(w, text='r4, c1', width=10).grid(row=4, column=1)
Button(w, text='r5, c0', width=10).grid(row=5, column=0)
Button(w, text='r5, c1', width=10).grid(row=5, column=1)
bt1.grid(row=3, column=0, columnspan=2)  # columnspan
w.mainloop()
