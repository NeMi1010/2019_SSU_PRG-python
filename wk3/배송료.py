Country = input("국가를 입력하시오 : ")
City = input("시를 입력하시오 : ")

if Country == '한국' :
    if City == '제주시' :
        print("배송료는 5000원입니다.")
    else :
        print("배송료는 10000원입니다.")
else :
    print("배송료는 20000원입니다.")

