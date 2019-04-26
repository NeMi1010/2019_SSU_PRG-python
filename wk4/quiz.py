from random import *
A = randint(1, 100)
B = randint(1, 100)

while True :
    ans = int(input("%d" % A + " + %d의 값은? : " % B))
    if(A+B == ans) : break
    print("틀렸습니다.")

print("맞았습니다.")
