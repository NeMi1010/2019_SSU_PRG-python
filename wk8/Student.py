class Scoremanager :
    def __init__(self, Score=[], Total=0, Student=0):
        self.__Score = Score
        self.__Total = Total
        self.__Student = Student

    def setScore(self, x):
        self.__Score.append(x)
        self.__Total += x
        self.__Student += 1

    def getAvg(self):
        return self.__Total // self.__Student

    def getStudent(self):
        return self.__Student

## main
if __name__ == 'main':
    DB = Scoremanager()
    print("학생성적관리 프로그램이 시작되었습니다.")
    while True :
        Menu = int(input("메뉴를 입력하세요 : "))
        if Menu == 1 :
            while True :
                Score_input = int(input("성적을 입력하세요. 종료하려면 -1을 입력하세요 : "))
                if Score_input == -1 :
                    break
                DB.setScore(Score_input)
        elif Menu == 2 :
            Average = DB.getAvg()
            print("평균점수는 %d점입니다." % Average)
        elif Menu == 3 :
            Students = DB.getStudent()
            print("학생수는 %d명입니다." % Students)

