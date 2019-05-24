import random

Q = list()
for i in range(10) :
    Q.append(random.randint(0, 101)*-1)

print(sorted(Q))

Q.sort(key=abs)
print(Q)
