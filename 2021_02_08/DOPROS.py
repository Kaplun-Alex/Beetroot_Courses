from tkinter import *
import tkinter.font
import datetime

win = tkinter.Tk()
win.title("DOPROS")
win.geometry('600x450+100+100')
ButtonFont = tkinter.font.Font(family='Hervetica', size=10, weight='bold')
BigFont = tkinter.font.Font(family='Hervetica', size=20, weight='bold')

d = datetime.date.today()
print(d)


def zahavay():  # перевірка на число в полі вік
    try:
        x = userEntry1.get()
        vik = int(x)
        if vik <= 16:
            year = 2021 - vik
            stryear = str(year)
            line1 = str('ти малолэтка  ' + stryear + '-го року народження.')
            statusentry.delete(0, END)
            statusentry.insert(0, line1)
        else:
            year = 2021 - vik
            stryear = str(year)
            line2 = str(stryear + '-го року народження.')
            statusentry.delete(0, END)
            statusentry.insert(0, 'старе пердло ' + line2)

    except ValueError:
        statusentry.delete(0, END)
        statusentry.insert(0, 'Ти дно, введи вік цифрами!')

    try:
        z = statusentry.get()
        if z == 'Ти дно, введи вік цифрами!':
            statusentry.delete(0, END)
            statusentry.insert(0, 'Ти дно, введи вік цифрами!')
        else:
            y = userEntry2.get()
            if y == "Ім'я":
                statusentry.delete(0, END)
                statusentry.insert(0, "Ти що хильнув зайвого, введи своє Ім'я!")
            else:
                znach = int(y) / 1
                statusentry.delete(0, END)
                statusentry.insert(0, "Ти дно, введи своє ім'я буквами!")
    except:
        name = userEntry2.get()
        statusentry.insert(0, name + '  ')


doprosbot = Label(win, text='Привіт братуха, як тебе звуть та скільки років маєш?', font=ButtonFont)
doprosbot.pack()
doprosbot.place(x=130, y=50)

datelabel = Label(win, text=d)
datelabel.pack()
datelabel.place(x=5, y=10)

userEntry1 = Entry(win, font=ButtonFont)
userEntry1.pack()
userEntry1.place(x=250, y=100, height=30, width=100)
userEntry1.delete(0, END)
userEntry1.insert(0, 'Вік братухи')

userEntry2 = Entry(win, font=ButtonFont)
userEntry2.pack()
userEntry2.place(x=250, y=150, height=30, width=100)
userEntry2.delete(0, END)
userEntry2.insert(0, "Ім'я")

statusline = Label(win, text='Статус', font=ButtonFont)
statusline.pack()
statusline.place(x=50, y=380)

statusentry = Entry(win, font=ButtonFont)
statusentry.pack()
statusentry.place(x=100, y=380, height=25, width=400)

skbut = Button(win, text='Твій тезультат', font=BigFont, command=zahavay)
skbut.pack()
skbut.place(x=180, y=250)

mainloop()
# Питання як перевіряти символи при вводі в поле Entry для мене залишається відкритим.... По факту в поля необхідно заборонити
# вводити літери або цифри, тоді відпадає перевірка на число і на кляті відємні значення.
