import time
import random
from tkinter import *
from tkinter.font import Font

def callback(event) :
    global Current_X, Current_Y, Size, Score, F, Stage
    if Current_X <= event.x <= Current_X+Size and Current_Y <= event.y <= Current_Y+Size :
        Score += 10
        LB_Score["text"] = "Score = " + str(Score)
        F = True
    Stage = (Score // 100) + 1
    LB_Stage["text"] = "Stage = " + str(Stage)
    

if __name__ == "__main__" :
    
    wd = Tk()
    wd.title("뭔지 모르는 클릭 게임")
    ft = Font(family="맑은 고딕", size="24")
    
    LB_Score = Label(wd, text="Score = 0", font=ft)
    LB_Stage = Label(wd, text="Stage = 1", font=ft)
    Draw = Canvas(wd, width=800, height=600)
    Draw.pack(anchor=S)
    LB_Stage.pack(anchor=N, side="left")
    LB_Score.pack(anchor=N, side="right")
    wd.resizable(False, False)

    Stage = 1
    Score = 0
    while True :

        F = False
        Speed = 2+Stage*4
        Size = 500 // Speed

        rand_x = random.randrange(0, 801-Size)
        Square = Canvas.create_rectangle(Draw, rand_x, 0, rand_x+Size, Size, fill="green")

        for i in range((600-Size)//Speed) :
            Current_X = rand_x
            Current_Y = i*Speed
            Draw.move(Square, 0, Speed)
            Draw.bind("<Button-1>", callback)
            if F == True :
                break
            wd.update()
            time.sleep(0.05)
        Draw.delete(Square)
        wd.update()
