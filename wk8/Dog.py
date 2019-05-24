class Dog :
    def __init__(self, Touched=0, Out=None) :
        self.__Touched = Touched
        self.__Out = Out

    def setTouched(self, click):
        self.__Touched = click

    def setOut(self, Out):
        self.__Out = Out

    def getOut(self):
        return self.__Out

Doggy = Dog()
Click = input("Clicked : ")

if Click == '귀' :
    Doggy.setOut("귀를 쫑긋한다")
elif Click == '입' :
    Doggy.setOut("멍멍 짓는다")
elif Click == '발' :
    Doggy.setOut("뒹군다")

result = Doggy.getOut()
print(result)
