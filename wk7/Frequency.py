string = input("문자열 : ")

# count() 미사용
cnt = 0
for ch in string :
    if ch is 'o' :
        cnt += 1
print(cnt)

# count() 사용
cnt = 0
cnt = string.count('o')
print(cnt)

