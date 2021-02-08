spisok = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
summ = 0
while spisok != []:
    if spisok[0] < 0:
        summ += spisok[0]
    del spisok[0]
print(summ)
