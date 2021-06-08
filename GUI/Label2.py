import tkinter


from tkinter import *
top = Tk()

rock = tkinter.PhotoImage(file='rock.png')
lb1 = Label(top, image=rock).pack(side='left')
# lb1 = Label(top, padx = 10, compound = CENTER,
#           text = txt, image=rock).pack(side='right') #compound로 사진 위에 텍스트

txt = '''A GUI is a type of user
interface that allows users
to interact with devices
in a graphic way.'''

lb2 = Label(top, padx=10, text=txt).pack(side='right')  # 가운데 정렬
# lb2 = Label(top, padx = 10, justify=LEFT,
#           text = txt).pack(side='right) #justify로 왼쪽 맞춤

top.mainloop()
