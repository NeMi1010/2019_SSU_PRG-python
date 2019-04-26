def process(w) :
    output = ""
    for ch in w :
        if ch.isalpha() :
            output += ch

    return output.lower()

words = set()

file_name = input("입력 파일 이름 : ")
fp = open(file_name, "r")

for line in fp :
    lineWords = line.split()
    for w in lineWords :
        words.add(process(w))

print("사용된 단어의 개수 = ", len(words))
print(words)
