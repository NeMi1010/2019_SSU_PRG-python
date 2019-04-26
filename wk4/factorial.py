'''

f = 1
N = int(input("N = "))

for i in range(1, N) :
    f *= N

print("%d" % f)

'''

f = 1
i = 0
N = int(input("N = "))

while i != N :
    i += 1
    f *= i

print("%d" % f)
