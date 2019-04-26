N = int(input("decimal = "))
a = ""

while N :
    a = str(N%2) + a
    N //= 2

print("binary : %s" % a)
