def birthday(ch) :
    year=""
    month=""
    day=""
    i = 0

    for x in ch :
        i += 1
        if x.isnumeric() :
            if i <= 4 :
                year += x
            elif i <= 6 :
                month += x
            else :
                day += x
        else :
            return (0, 0, 0)

    return (year, month, day)

day = []
for i in range(1, 13) :
    if i == 2 :
        day.append(28)
    elif i <= 7 :
        day.append(30+i%2)
    else :
        day.append(31-i%2)


date = input("생년월일 : ")
(Y, M, D) = birthday(date)

if Y == 0 or int(M) > 12 or int(M) < 1 or int(day[int(M)-1]) < int(D):
    print("올바른 입력이 아닙니다")
else :
    print("%d년 %d월 %d일생" % (int(Y), int(M), int(D)))
