kor = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
a = []
i = 0
j = 0
while i < len(kor):
    if kor[i] == 2:
        a.insert(j, i)
        j += 1
    i += 1

print(a)
