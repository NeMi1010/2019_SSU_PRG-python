Person = dict()

while True :
    print()
    ID = input("ID : ")
    if ID not in Person :
        PW = input("Password : ")
        Person[ID] = PW
    else :
        print("Password : %s" % Person[ID])
