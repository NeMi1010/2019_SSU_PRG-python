# 5

score = list()
sum = 0
avg = 0.0
count = 0
for i in range(5) :
    score.append(input("점수를 입력하세요 : "))
    sum += int(score[i])

avg = sum/5
for i in range(5) :
    if float(score[i]) >= avg : count += 1
print("평균 = %.1f" % avg)
print("평균 이상의 학생 수 = %d" % count)
