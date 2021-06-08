from tkinter import *
from time import *
from tkinter.messagebox import showinfo  # window에 출력함을 위함


def clicked():  # callback 함수
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    print(time)
    showinfo(message=time)  # 이거 없으면 콘솔 창에 출력됨


root = Tk()

button = Button(root, text='Click it', command=clicked)
button.pack()

root.mainloop()
