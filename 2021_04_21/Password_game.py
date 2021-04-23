from tkinter import *
import tkinter.font
import random

win = tkinter.Tk()
win.title("DOPROS")
win.geometry('600x450+100+100')
ButtonFont = tkinter.font.Font(family='Hervetica', size=12, weight='bold')
BigFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')

def ok_button_f(event):
    mes = pasword.get()
    if mes != '':
        user.delete(0, END)
        user.insert(0, 'Тепер я знаю твій пароль! LOL!')
        pasword.delete(0, END)
        pasword.insert(0, 'Тепер я знаю твій пароль! LOL!')
        ok_button.place_configure(x=random.randint(5, 450), y=random.randint(130, 350))
    else:
        pass


user = Entry(win, font=ButtonFont, justify='center', width=40)
user.pack()
user.place(x=150, y=50)

user_lab = Label(win, text='User:', font=ButtonFont)
user_lab.pack()
user_lab.place(x=20, y=50)

pasword = Entry(win, font=ButtonFont, justify='center', width=40)
pasword.pack()
pasword.place(x=150, y=100)

pasword_lab = Label(win, text='Password:', font=ButtonFont)
pasword_lab.pack()
pasword_lab.place(x=20, y=100)

ok_button = Button(win, text='OK', font=BigFont, width=6)
ok_button.pack()
ok_button.bind('<Enter>', ok_button_f)
ok_button.place(x=250, y=200)
win.after(30000, win.destroy)
mainloop()