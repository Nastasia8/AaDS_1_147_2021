kor = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
res = []
i = 0
j = 0

while i <= 9:
    if kor[i] == 2:
        res.insert(j, i)
        j += 1
    i += 1
    
print(res)
