'''
import random

stk = bal = num = 0 # 변수 초기화
chk = [] # 숫자 유무 체크리스트
lis = []
for i in range(10) :
    lis.append(str(i))
    chk.append(0)

random.shuffle(lis)
ans = lis[0]+lis[1]+lis[2]+lis[3] # 배열 섞은 이후 앞 4자리 문자열화

while num < 5 : # 최대 5번 실행
    num += 1
    stk = bal = 0 # 각 입력마다 결과값 초기화
    n = input("숫자를 입력하세요 : ")
    for i in range(4) :
       chk[int(ans[i])] += 1

  # 입력값과 정답 비교
    for i in range(4) :
        if ans[i] == n[i] :
            stk += 1
        elif not chk[int(n[i])] == 0 :
            bal += 11
            chk[int(n[i])] -= 1

  # 출력
    if(stk == 4) : print("4 스트라이크 입니다. 정답", end='')
    elif(stk == 0 and bal == 0) : print("아웃", end='')

    if(stk != 0 and stk != 4) : print("%s 스트라이크" % stk, end=' ')
    if(bal != 0) : print("%s 볼" % bal, end=' ')
    print("입니다.", end='\n\n')

    if(stk == 4) : break

print("정답은", end=' ')
if(lis[0]=='0') : print('0', end='')
print("%s입니다." % ans)

'''

import random

stk = bal = num = 0 # 변수 초기화
chk = [] # 숫자 유무 체크리스트
lis = []
for i in range(10) :
    lis.append(str(i))
    chk.append(0)

random.shuffle(lis)
ans = int(lis[0]+lis[1]+lis[2]+lis[3]) # 배열 섞은 이후 앞 4자리 정수화

while num < 5 : # 최대 5번 실행
    num += 1
    stk = bal = 0 # 각 입력마다 결과값 초기화
    n = int(input("숫자를 입력하세요 : "))
    for i in range(4) :
        a = ans // (10**i) % 10
        chk[a] += 1

  # 입력값과 정답 비교
    for i in range(4) :
        a = ans // (10**i) % 10
        b = n // (10**i) % 10
        if a == b :
            stk += 1
        elif not chk[b] == 0 :
            bal += 1
            chk[b] -= 1

  # 출력
    if(stk == 4) : print("4 스트라이크 입니다. 정답", end='')
    elif(stk == 0 and bal == 0) : print("아웃", end='')

    if(stk != 0 and stk != 4) : print("%s 스트라이크" % stk, end=' ')
    if(bal != 0) : print("%s 볼" % bal, end=' ')
    print("입니다.", end='\n\n')

    if(stk == 4) : break

print("정답은", end=' ')
if(lis[0]=='0') : print('0', end='')
print("%s입니다." % ans)
