from tkinter import *
        
def USA_act(x) :
    Country[x] += 1
    USA['text'] = x+":"+str(Country[x])

def UK_act(x) :
    Country[x] += 1
    UK['text'] = x+":"+str(Country[x])

def FR_act(x) :
    Country[x] += 1
    FR['text'] = x+":"+str(Country[x])

def JP_act(x) :
    Country[x] += 1
    JP['text'] = x+":"+str(Country[x])


Country = {"미국":0, "영국":0, "프랑스":0, "일본":0}
if __name__ == "__main__" :

    WD = Tk()

    QNA = Label(WD, text="가장 여행하고 싶은 나라는?")
    QNA.pack()
        
    USA = Button(WD, text="미국:0", command=lambda N="미국":USA_act(N))
    USA.pack(anchor="w")

    UK = Button(WD, text="영국:0", command=lambda N="영국":UK_act(N))
    UK.pack(anchor="w")

    FR = Button(WD, text="프랑스:0", command=lambda N="프랑스":FR_act(N))
    FR.pack(anchor="w")

    JP = Button(WD, text="일본:0", command=lambda N="일본":JP_act(N))
    JP.pack(anchor="w")
