list = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
new_list = []

find = 2
i = 0
for k in list:
    if k == find:
        print('Значение:', k, 'Индекс:', i)
        new_list.append(i)
    i += 1
print(new_list)
