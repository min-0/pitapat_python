from tkinter import *

w = Tk()

lblist = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]

for r in range(4):
    for c in range(3):
        lbLabel = Label(w, relief=RAISED, padx=10, text=lblist[r][c])
        lbLabel.grid(row=r, column=c)

w.mainloop()
