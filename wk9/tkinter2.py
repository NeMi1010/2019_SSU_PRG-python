from tkinter import *
import random

def chk(k) :
    global Blank, count
    Clicked = Btn_list[k]

    if Clicked["text"] != Blank :
        return
    Clicked["text"] = 'O'.center(3)
    if count == 4 :
        return
    else :
        count += 1

    while True :
        input = random.randrange(0, 9)
        CPU = Btn_list[input]
        if CPU["text"] == Blank :
            CPU["text"] = 'X'.center(3)
            return


Btn_list = list()
wd = Tk()
Blank = ' -- '
count = 0

for i in range(9) :
    Bingo = Button(wd, text=Blank, command = lambda k = i : chk(k))
    Bingo.grid(row=i//3, column=i%3)
    Btn_list.append(Bingo)



wd.mainloop()
