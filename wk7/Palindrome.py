string = input("문자열 : ")
reversed_str = ''.join(reversed(string))

# reversed() 미사용
chk = True
for i in range(len(string)//2) :
    if string[i] is not string[len(string)-i-1] :
        chk = False
        break

if chk :
    print("회문입니다")
else :
    print("회문이 아닙니다")

# reversed() 사용
if string == reversed_str :
    print("회문입니다")
else :
    print("회문이 아닙니다")
