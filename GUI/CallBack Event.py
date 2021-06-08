from tkinter import *

top = Tk()


def ft():
    global cnt
    cnt += 1
    lb['text'] = str(cnt) + '번 클릭했습니다!'


cnt = 0
lb = Label(top)
lb.pack()

button = Button(top, text="클릭하세요!", command=ft)
button.pack()

top.mainloop()
