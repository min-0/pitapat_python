from tkinter import *

top = Tk()
top.title('스톱 워치')

cnt = 0


def Stopwatch():
    if running:
        global cnt
        cnt += 1
        lb1.config(text=str(cnt))
    top.after(1000, Stopwatch)


def Start():
    global running
    running = True


def Stop():
    global running
    running = False


def Reset():
    global cnt
    cnt = 0
    lb1.config(text=str(cnt))


lb1 = Label(top, font=('Helvetica', 20), fg='red')
lb1.pack()

running = False
Stopwatch()

bt1 = Button(top, text='Start', width=25, command=Start)
bt2 = Button(top, text='Stop', width=25, command=Stop)
bt3 = Button(top, text='Reset', width=25, command=Reset)

bt1.pack()
bt2.pack()
bt3.pack()

top.mainloop()
