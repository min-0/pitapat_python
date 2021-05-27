from tkinter import *
from time import strptime, strftime
from tkinter.messagebox import showinfo

# strptime(): 문자열 date를 지정된 포맷의 날짜 data로 변한
# strftime(): 날짜 data를 지정된 포맷으로 변환하여 반환(%A = 요일)


def compute():
    global dateEnt

    date = dateEnt.get()  # 엔트리 내의 문자열 반환
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))
    showinfo(message='{} was a {}'.format(date, weekday))
    dateEnt.delete(0, END)


root = Tk()

# label
label = Label(root, text="Enter date")
label.grid(row=0, column=0)

# entry
dateEnt = Entry(root)
dateEnt.grid(row=0, column=1)

# button
button = Button(root, text='Enter', command=compute)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()
