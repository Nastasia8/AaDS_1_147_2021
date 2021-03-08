Numbers = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
Solution = []

find = 2
i = 0
for k in Numbers:
    if k == find:
        print('Значение:', k, 'Индекс:', i)
        Solution.append(i)
    i += 1
print(Solution)
