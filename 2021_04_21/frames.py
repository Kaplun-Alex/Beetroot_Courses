from tkinter import *
import tkinter.font

win = tkinter.Tk()
BigFont = tkinter.font.Font(family='Hervetica', size=8, weight='bold')
win.title("FRAMES")
win.geometry('500x500+10+10')

frame1 = tkinter.Frame(win, padx = 50, pady=50,  background='black')
frame1.pack(anchor='ne', side='left')
frame1.place(x=10, y=10)#must be n, ne, e, se, s, sw, w, nw, or center

ok_button11 = Button(frame1, text='OK', font=BigFont, width=3)
ok_button11.grid(row=0, column=0)
ok_button12 = Button(frame1, text='OK', font=BigFont, width=3)
ok_button12.grid(row=0, column=500)
ok_button13 = Button(frame1, text='OK', font=BigFont, width=3)
ok_button13.grid(row=2589, column=500)


frame2 = tkinter.Frame(win, padx = 50, pady=50,  background='black')
frame2.pack(anchor='nw', side='right')
ok_button21 = Button(frame2, text='OK', font=BigFont, width=3)
ok_button21.grid(row=0, column=0)

frame3 = tkinter.Frame(win, padx = 50, pady=50,  background='black')
frame3.pack(anchor='center', side='bottom')

ok_button31 = Button(frame3, text='OK', font=BigFont, width=3)
ok_button31.grid(row=0, column=0)


win.mainloop()



