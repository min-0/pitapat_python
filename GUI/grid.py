from tkinter import *

w = Tk()

Bbt = Button(w, text='아래쪽', padx=10).pack(side=BOTTOM)  # bottom은 먼저 해줘야 할 듯
Tbt = Button(w, text='위쪽', padx=10).pack()
Lbt = Button(w, text='왼쪽', padx=10).pack(side=LEFT)
Rbt = Button(w, text='오른쪽', padx=10).pack(side=LEFT)

w.mainloop()
