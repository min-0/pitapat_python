from tkinter import *
from calendar import monthrange
# 9.2 실습문제

w = Tk()

dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

for i in range(7):
    lb = Label(w, text=dayList[i])
    lb.grid(row=0, column=i)

weekday, numDays = monthrange(2021, 5)
week = 1

for i in range(1, numDays+1):
    lb2 = Label(w, text=str(i))
    lb2.grid(row=week, column=weekday)

    weekday += 1.
    if weekday > 6:
        week += 1
        weekday = 0
w.mainloop()
