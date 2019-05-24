from tkinter import *
from tkinter.font import *

def size_up() :
    bt_font['size'] += 2

def size_down() :
    bt_font['size'] -= 2

window = Tk()
bt_font = Font(window, "Helvetica", size=10)
Word = Label(window, text="폰트 크기", font=bt_font)

smaller = Button(window, text="작게", command=size_down)
bigger = Button(window, text="크게", command=size_up)
Word.pack()
smaller.pack(side=LEFT)
bigger.pack(side=RIGHT)



window.mainloop()
