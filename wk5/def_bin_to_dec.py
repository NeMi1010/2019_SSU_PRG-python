# 6

def bin_to_dec(bin) :
    n = 1
    sum = 0
    i = len(bin)
    while i :
        i -= 1
        sum += n * int(bin[i])
        n *= 2

    return sum

x = str(input("2진수 : "))
print("10진수 : %d" % bin_to_dec(x))
print(x)

