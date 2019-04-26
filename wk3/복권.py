'''

import random

N = str(random.randrange(1, 99))
In = input("복권 번호 : ")
cnt = 0

for i in range(0, 1) :
    if In[i] == N[i] :
        cnt += 1

print("%s만원을 획득하셨습니다" % (cnt * 50))
print("복권 번호 : ", N)

'''

import random

N = random.randrange(1, 99)
n1 = N//10
n2 = N%10

In = int(input("복권 번호 : "))
In1 = In//10
In2 = In%10
cnt = 0

if n1 == In1 :
    cnt += 1
if n2 == In2 :
    cnt += 1

print("%s만원을 획득하셨습니다" % (cnt * 50))
print("복권 번호 : ", N)
