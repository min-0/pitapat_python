from tkinter import *

top = Tk()  # 창 같은 거 만듦
top.title("BMI 계산")  # 메인 윈도우 타이틀


def calc():
    height = float(en1.get())
    weight = float(en2.get())
    bmi = weight / height ** 2
    en1.delete(0, END)
    en2.delete(0, END)
    en3.insert(0, bmi)
    lb4["text"] = str(bmi)


# 4개의 레이블, 2개의 입력 엔트리, 1개의 버튼 need -> 격자 모양 틀 구성
lb1 = Label(top, text="키(m)")
lb2 = Label(top, text="BMI")
lb3 = Label(top, text="몸무게(kg)")
lb4 = Label(top)
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=2)
lb3.grid(row=1, column=0)
lb4.grid(row=1, column=2)

en1 = Entry(top)
en2 = Entry(top)
en3 = Entry(top)
en1.grid(row=0, column=1)
en2.grid(row=1, column=1)
en3.grid(row=1, column=2)

bt1 = Button(top, width=10, text="계 산", command=calc)  # 계산을 위해 함수 호출
bt1.grid(row=2, column=2)

top.mainloop()
