import random

def bingo_check() :
    global chk
    for i in range(0, 5) :
        check = chk[i]
        result = True
        for j in range(i+5, 25, 5) :
            if not chk[j] == check :
                result = False
                break
        if result :
            return result, check

    for i in range(0, 5) :
        check = chk[i]
        result = True
        for j in range(i*5,i*5+5) :
            if not chk[j] == check :
                result = False
                break
        if result :
            return result, check

    check = chk[0]
    result = True
    for j in range(0, 25, 6) :
        if not chk[j] == check :
            result = False
            break
    if result :
        return result, check

    check = chk[4]
    result = True
    for j in range(4, 24, 4) :
        if not chk[j] == check :
            result = False
            break
    if result :
        return result, check

    return False, 0

chk = list()
count = 25
for i in range(0, 25) :
    chk.append(i)

while True :
    for x in range(0, 25) :
        if chk[x] == -1 :
            print(" -X", end='')
        elif chk[x] == -2 :
            print(" -O", end='')
        else :
            print("%3d" % chk[x], end='')

        if (x+1) % 5 == 0 :
            print()

    while True :
        num = int(input("번호를 선택하세요 : "));
        if not chk[num] == -1 and not chk[num] == -2 :
            break
    chk[num] = -1
    count -= 1
    if not count :
        break

    res, number = bingo_check()
    if res :
        for x in range(0, 25) :
            if chk[x] == -1 :
                print(" -X", end='')
            elif chk[x] == -2 :
                print(" -O", end='')
            else :
                print("%3d" % chk[x], end='')

            if (x+1) % 5 == 0 :
                print()
        print("\n빙고!", end='')
        if number == -1 :
            print("이겼습니다.")
        else :
            print("졌습니다.")

        break

    while True :
        ranum = random.randrange(0, 25)
        if not chk[ranum] == -1 and not chk[ranum] == -2 :
            break
    chk[ranum] = -2
    count -= 1
