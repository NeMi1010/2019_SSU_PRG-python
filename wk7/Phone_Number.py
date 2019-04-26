def Insert() :
    global Book

    while True :
        Name = input("(입력모드) 이름을 입력하세요 : ")
        if Name is '' :
            break
        Pnum = input("(입력모드) 전화번호를 입력하세요 : ")
        if Pnum is '' :
            break

        Book[Name] = Pnum

def Search() :
    global Book

    while True :
        Name = input("\n(검색모드) 이름을 입력하세요 : ")
        if Name in Book :
            print("(검색모드) 전화번호는 %s 입니다" % Book[Name])
            return
        print("(검색모드) 찾는 이름이 없습니다.")

Book = dict()

Insert()
Search()
