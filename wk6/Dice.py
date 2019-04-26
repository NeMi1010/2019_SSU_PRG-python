# 6

import random

def dice() :
    num = random.randrange(6)
    return num

N = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    k = dice()
    N[k] += 1

for i in range(0, 6) :
    print("주사위가 %d 인 경우는 %d 번" % (i+1, int(N[i])))
