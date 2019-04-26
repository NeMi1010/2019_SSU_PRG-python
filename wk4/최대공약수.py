x = int(input("x? = "))
y = int(input("y? = "))
i = 0

while 1 :
    i += 1
    if i == x or i == y : break
    if not x % i and not y % i : ans = i

print(ans)
