string = input("문자열 : ")
rev_str = ''.join(reversed(string))

# reversed() 미사용
for i in range(len(string)-1, -1, -1) :
    print(string[i], end='')                        # print(string[::-1])
print()

# reversed() 사용
print(rev_str)
