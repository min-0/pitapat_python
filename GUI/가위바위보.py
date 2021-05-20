from tkinter import *
from tkinter.font import Font
import random

rsp = Tk()
rsp.title("가위 바위 보 게임")

bt_list = ['가위', '바위', '보']

Rockphoto = PhotoImage(file='rock.png')
Scissorphoto = PhotoImage(file='scissor.png', height=190)
Paperphoto = PhotoImage(file='paper.png', height=198)

lb1 = Label(rsp)
lb2 = Label(rsp)
lb3 = Label(rsp, text='사용자')
lb4 = Label(rsp, text='컴퓨터')
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=2)
lb3.grid(row=1, column=0)
lb4.grid(row=1, column=2)

rst = Label(rsp, text='게임 결과', fg='green', font=Font(size=20))
rst.grid(row=0, column=1)


def result(num, img):
    if num == 1:
        lb1 = Label(rsp, image=img)
        lb1.grid(row=0, column=0)
    elif num == 2:
        lb2 = Label(rsp, image=img)
        lb2.grid(row=0, column=2)


def game(choice):
    if choice == 0:
        choice = '가위'
    elif choice == 1:
        choice = '바위'
    else:
        choice = '보'

    com = random.choice(['가위', '바위', '보'])
    if com == '가위':
        result(2, Scissorphoto)
    elif com == '바위':
        result(2, Rockphoto)
    elif com == '보':
        result(2, Paperphoto)

    temp = '출력'
    if choice == '가위':
        result(1, Scissorphoto)
        if com == '가위':
            temp = '무승부'
        elif com == '바위':
            temp = '컴퓨터 승'
        elif com == '보':
            temp = '사용자 승'
    elif choice == '바위':
        result(1, Rockphoto)
        if com == '가위':
            temp = '사용자 승'
        elif com == '바위':
            temp = '무승부'
        elif com == '보':
            temp = '컴퓨터 승'
    elif choice == '보':
        result(1, Paperphoto)
        if com == '가위':
            temp = '컴퓨터 승'
        elif com == '바위':
            temp = '사용자 승'
        elif com == '보':
            temp = '무승부'
    rst['text'] = temp


i = 0
for btText in bt_list:
    def click(t=i):
        game(t)
    Button(rsp, text=btText, width=30,
           command=click, bg='yellow').grid(row=3, column=i)
    i = i + 1

rsp.mainloop()
