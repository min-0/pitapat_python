from tkinter import *

top = Tk()

click = PhotoImage(file='rock.png')
bt = Button(top, image=click, text='클릭하세요!', compound=LEFT)
# compound가 없으면 text 안나옴 주의
bt.pack()

top.mainloop()
