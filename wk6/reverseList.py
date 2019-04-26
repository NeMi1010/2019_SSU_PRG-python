# 4

'''
def reverseList(List) :
    A = list()
    List.sort()
    for i in range(len(List)) : A.append(List.pop())
    return A

customer = list()
for i in range(5) : customer.append(input("고객이름 : "))
print(reverseList(customer))
'''

def reverseList(List) :
    List.sort(reverse=True) # List.sort() + List.reverse()
    return List

customer = list()
for i in range(5) : customer.append(input("고객이름 : "))
print(reverseList(customer))
