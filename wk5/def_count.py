# 2

count = 0
def inc() :
    global count
    count += 1

n = int(input("관람객 인원 : "))
for i in range(0, n) :
    inc()

print(count)
