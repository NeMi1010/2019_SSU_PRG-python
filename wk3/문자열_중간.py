CH = input("문자열을 입력하시오 : ")
n = len(CH)

if(n%2) :
    print("중앙글자는", CH[n//2])
else :
    print("중앙글자는", CH[n//2-1]+CH[n//2])
