# 5

'''
def get_filtered(a, b) :

    ans = ""
    for i in range(0, len(a)) :
        f = True
        for j in range(0, len(b)) :
            if a[i] == b[j] :
                f = False
                break
        if f :
            ans += a[i]

    return ans

////////////////////////////////////

def get_filtered(a, b) :

    for i in range(0, len(b)) :
        a = a.replace(b[i], "")

    return a

x = input("문장을 입력하세요 : ")
y = "$#!?_-'"
print("%s" % get_filtered(x, y))

////////////////////////////////////
'''

def get(a, b) :
    for i in a :
        if i not in b :
            print(i, end='')

x = input("문장을 입력하세요 : ")
y = "$#!?_-'"
get(x, y)


