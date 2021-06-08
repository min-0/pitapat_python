from tkinter import *

top = Tk()
top.title('체크버튼')


def draw():
    if v1.get() == 1:
        canvus.create_rectangle(20, 10, 280, 90, tags='v1')
    else:
        canvus.delete('v1')
    if v2.get() == 1:
        canvus.create_oval(20, 10, 280, 90, tags='v2')
    else:
        canvus.delete('v2')
    if v3.get() == 1:
        canvus.create_line(20, 10, 280, 90, tags='v3')
    else:
        canvus.delete('v3')


canvus = Canvas(top, height=100, width=300, bg='white', borderwidth=3)
canvus.pack()

frm = Frame(top)
frm.pack()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

check1 = Checkbutton(frm, text='직사각형', variable=v1, command=draw)
check2 = Checkbutton(frm, text='타 원', variable=v2, command=draw)
check3 = Checkbutton(frm, text='직 선', variable=v3, command=draw)

check1.pack(side=LEFT)
check2.pack(side=LEFT)
check3.pack(side=LEFT)

top.mainloop()
