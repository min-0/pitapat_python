from tkinter import *

root = Tk()

photo = PhotoImage(file='rock.png')  # 가져올 이미지 파일

peace = Label(master=root,
              image=photo,
              width=300,
              height=180)
peace.pack()
root.mainloop()
