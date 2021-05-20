from tkinter import *
# label을 통한 출력

window = Tk()

# window의 자식 label 위젯 생성
label = Label(window, text="Hello GUI world!",
              width=20, height=2,
              font='helvetica 14 italic',
              relief=RAISED)
label.pack()  # 배치

# lb = Label(window)
# lb['text'] = "Hello GUI world!"
# lb['width'] = 20
# lb['height'] = 2
# lb['font'] = 'helvetica 14 italic'
# lb['relief'] = RAISED #입체적 효과

# lb.pack()

window.mainloop()
