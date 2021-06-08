from tkinter import *

top = Tk()
top.title('라디오버튼과 체크버튼')


def draw():
    canvus.delete(ALL)
    if v1.get() == 1:
        if v.get() == 'rect':
            canvus.create_rectangle(20, 10, 280, 90, fill='yellow')
        if v.get() == 'oval':
            canvus.create_oval(20, 10, 280, 90, fill='yellow')
        if v.get() == 'line':
            canvus.create_line(20, 10, 280, 90)
    else:
        if v.get() == 'rect':
            canvus.create_rectangle(20, 10, 280, 90)
        if v.get() == 'oval':
            canvus.create_oval(20, 10, 280, 90)
        if v.get() == 'line':
            canvus.create_line(20, 10, 280, 90)


canvus = Canvas(top, width=300, height=100, bg='white', borderwidth=3)
canvus.pack()

frm = Frame(top)
frm.pack()

v = StringVar()
v1 = IntVar()

rb1 = Radiobutton(frm, text="직사각형", variable=v, value='rect', command=draw)
rb2 = Radiobutton(frm, text="타 원", variable=v, value='oval', command=draw)
rb3 = Radiobutton(frm, text="직 선", variable=v, value='line', command=draw)
cb1 = Checkbutton(frm, text='색 채우기', variable=v1, command=draw)

rb1.pack(side=LEFT)
rb2.pack(side=LEFT)
rb3.pack(side=LEFT)
cb1.pack(side=LEFT)

top.mainloop()
