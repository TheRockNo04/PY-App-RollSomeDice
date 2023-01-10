from tkinter import *
from PIL import ImageTk,Image
import Script
import os
import random as rn

root = Tk()

e = Entry(root)
e.grid(row=0, column=0, columnspan=2)

def sayHi():
    greet = Label(root, text="Hello " + e.get() + "!")
    greet.grid(column=0)

button1 = Button(root, text="Click Me!", command=sayHi)
button1.grid(row=1, column=0)


def roll_next():    
    for _ in range(1):
        die1 = rn.randint(1,6)
        img1 = ImageTk.PhotoImage(Image.open(f'Images\\{die1}.png'))
        lbl1 = Label(image=img1)
        lbl1.grid(row=2, column=0)

        die2 = rn.randint(1,6)
        img2 = ImageTk.PhotoImage(Image.open(f'Images\\{die2}.png'))
        lbl2 = Label(image=img2)
        lbl2.grid(row=2, column=1)

button2 = Button(root, text="Roll!", command=roll_next)
button2.grid(row=1, column=1)

die2 = rn.randint(1,6)
img = ImageTk.PhotoImage(Image.open(f'Images\\{die2}.png'))
lbl = Label(image=img)
lbl.grid(row=2, column=0)

root.mainloop()
