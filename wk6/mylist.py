# 1

mylist = [1, 2, 3, 4, 5, 6]

print(mylist[0])
for i in range(1, 5) : print(mylist[i], end=' ')
print("")
print(max(mylist))
print(min(mylist))

sum = 0
for i in range(len(mylist)) : sum += mylist[i]
print(sum)
print(mylist[-2])
