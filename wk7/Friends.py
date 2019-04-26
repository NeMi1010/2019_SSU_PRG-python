FRD = dict()

while True :
    print()
    NAME = input("Name : ")
    if NAME not in FRD :
        PHONE = input("Phone Number : ")
        FRD[NAME] = PHONE
    else :
        print("Phone Number : %s" % FRD[NAME])

