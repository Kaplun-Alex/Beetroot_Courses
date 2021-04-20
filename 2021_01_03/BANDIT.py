from tkinter import *
import tkinter.font
import random

rn = random.Random()
win = tkinter.Tk()
win.title("DOPROS")
win.geometry('600x450+100+100')
ButtonFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')
BigFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')


def run():
    userEntry1.delete(0, END)
    userEntry2.delete(0, END)
    userEntry3.delete(0, END)
    userEntry1.insert(0, rn.randint(0, 9))
    userEntry2.insert(0, rn.randint(0, 9))
    userEntry3.insert(0, rn.randint(0, 9))
    ge1 = userEntry1.get()
    ge2 = userEntry2.get()
    ge3 = userEntry3.get()
    if ge1 == ge2 == ge3:
        userEntry4.delete(0, END)
        userEntry4.insert(0, "YOU WIN")
    else:
        userEntry4.delete(0, END)
        userEntry4.insert(0, "LOOSER!")


doprosbot = Label(win, text='ОДНОРУКИЙ БАНДЮГАН', font=ButtonFont)
doprosbot.pack()
doprosbot.place(x=120, y=50)

userEntry1 = Entry(win, font=ButtonFont, justify='center')
userEntry1.pack()
userEntry1.place(x=100, y=100, height=60, width=50)
userEntry1.delete(0, END)
enum1 = rn.randint(0, 9)
userEntry1.insert(0, enum1)

userEntry2 = Entry(win, font=ButtonFont, justify='center')
userEntry2.pack()
userEntry2.place(x=250, y=100, height=60, width=50)
userEntry2.delete(0, END)
enum2 = rn.randint(0, 9)
userEntry2.insert(0, enum2)

userEntry3 = Entry(win, font=ButtonFont, justify='center')
userEntry3.pack()
userEntry3.place(x=400, y=100, height=60, width=50)
userEntry3.delete(0, END)
enum3 = rn.randint(0, 9)
userEntry3.insert(0, enum3)

userEntry4 = Entry(win, font=ButtonFont, justify='center')
userEntry4.pack()
userEntry4.place(x=180, y=200, height=60, width=200)
userEntry4.delete(0, END)
userEntry4.insert(0, '\|/')

skbut = Button(win, text='Жми та виграй', font=BigFont, command=run)
skbut.pack()
skbut.place(x=180, y=350)

mainloop()
