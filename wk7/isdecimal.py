while True :
    chk = True
    age = input("나이 : ")
    for ch in age :
        if not ch.isdecimal() :
            chk = False
            break
    if chk :
        break

print("당신의 나이는 %d세 입니다" % int(age))
