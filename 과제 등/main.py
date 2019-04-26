'''

import random

print("숫자게임에 오신 것을 환영합니다")
number = random.randint(1, 100)

for i in range(0, 10) :
    num = input("1부터 100 사이의 숫자를 입력해보세요 : ")
    guess = int(num)
    if guess > number :
        print(guess,"보다 작습니다.")
    elif guess < number :
        print(guess,"보다 큽니다.")
    else :
        print("맞았습니다.")
        break

if i < 10 :
    print("실패하셨습니다")

print("게임이 종료되었습니다.")

'''
