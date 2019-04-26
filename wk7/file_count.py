file_name = input("파일 이름 : ")
F = open(file_name, "r")

table = dict()
for line in F :
    words = line.split()
    for ch in words :
        if ch not in table :
            table[ch] = 1
        else :
            table[ch] += 1

print(table)
