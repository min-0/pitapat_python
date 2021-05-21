from tkinter import *

w = Tk()

b1 = Button(w, text='첫번째 버튼')
b2 = Button(w, text='두번째 버튼')
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
# side로 button left 정렬 default=TOP

b1['text'] = 'one'
# button text 변경

Button(w, text='Python 언어').pack(fill=X, padx=10)
Button(w, text='C++ 언어').pack(fill=X, padx=10, pady=5)
Button(w, text='Visual Basic 언어').pack(fill=X, padx=10)
# fill로 button size 맞추기, padding으로 space
w.mainloop()
