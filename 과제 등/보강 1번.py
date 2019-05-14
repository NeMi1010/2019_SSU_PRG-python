from tkinter import *

def CMD_Move(X, Y) :
    CV.move(SQ, X, Y)


if __name__ == "__main__" :

    WD = Tk()

    CV = Canvas(WD, bg="white", width=500, height=300)
    CV.grid(row=0, column=0, columnspan=4)

    SQ = CV.create_rectangle(100, 100, 200, 200, fill="red")
    

    Left = Button(WD, text="←(Left)", command=lambda x=-5, y=0:CMD_Move(x, y))
    Left.grid(row=1, column=0)

    Right = Button(WD, text="→(Right)", command=lambda x=5, y=0:CMD_Move(x, y))
    Right.grid(row=1, column=1)

    Up = Button(WD, text="↑(Up)", command=lambda x=0, y=-5:CMD_Move(x, y))
    Up.grid(row=1, column=2)

    Down = Button(WD, text="↓(Down)", command=lambda x=0, y=5:CMD_Move(x, y))
    Down.grid(row=1, column=3)

    WD.mainloop()
