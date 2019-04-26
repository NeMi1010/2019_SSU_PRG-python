Key = dict()

# A : 2, B : 2, C : 2, D : 3, E : 3, ...

for i in range(65, 91) :
    Key[chr(i)] = (i-59)//3
Key['S'] = 7
Key['V'] = 8
Key['Y'] = Key['Z'] = 9

string = input("문자열을 입력하시오 : ")
for ch in string :
    if ch.isalpha() :
        print("%d" % Key[ch], end='')
