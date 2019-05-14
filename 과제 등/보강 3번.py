from tkinter import *

class DB :

    global Q
    def __init__(self) :
        WD = Tk()

        self.label_name = Label(WD, text="이름")
        self.label_name.grid(row=0, column=0)
        self.Name = Entry(WD)
        self.Name.grid(row=0, column=1)

        self.label_job = Label(WD, text="직업")
        self.label_job.grid(row=1, column=0)
        self.Job = Entry(WD)
        self.Job.grid(row=1, column=1)

        self.label_country = Label(WD, text="국적")
        self.label_country.grid(row=2, column=0)
        self.Country = Entry(WD)
        self.Country.grid(row=2, column=1)

        self.save = Button(WD, text="저장", command=self.in_Save)
        self.label_save = Label(WD, text="저장할 데이터를 입력하세요")
        self.save.grid(row=3, column=0)
        self.label_save.grid(row=3, column=1)

        self.search = Button(WD, text="검색", command=self.out_Search)
        self.label_search = Label(WD, text="검색할 이름을 입력하세요")
        self.search.grid(row=4, column=0)
        self.label_search.grid(row=4, column=1)
    
    def in_Save(self) :
        Q[self.Name.get()] = (self.Job.get(), self.Country.get())
        print("{"+self.Name.get()+" : ",Q[self.Name.get()],"}")
        self.Name.delete(0, END)
        self.Job.delete(0, END)
        self.Country.delete(0, END)
        
    def out_Search(self) :
        if self.Name.get() in Q :
            print("찾았습니다 : ", Q[self.Name.get()])
            return
        print("찾는 이름이 없습니다")
        
    
Q = dict()
if __name__ == "__main__" :
    DB()
