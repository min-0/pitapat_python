from tkinter import *
root = Tk()

text = Label(root, font=('Helvetica', 16, 'bold italic'),
             foreground='white', background='black',
             padx=25, pady=10,
             text='Peace begins with a smile.')
text.pack(side=BOTTOM)

rock = PhotoImage(file='rock.png')
rockLabel = Label(root, borderwidth=3, relief=RIDGE, image=rock)
rockLabel.pack(side=LEFT)

paper = PhotoImage(file='paper.png')
paperLabel = Label(root, image=paper)
paperLabel.pack(side=RIGHT)

root.mainloop()

# option side를 이용해 TOP, BOTTOM, LEFT, RIGTH 배치
