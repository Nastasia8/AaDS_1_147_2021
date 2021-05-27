n = int(input()) #ввод кол-ва предметов
sort = []
for i in range (n):
    sort.append(input().split(" ")) #ввод предметов
sort = [[int(sort[i][j]) for j in range(2)] for i in range(n)] #распределение по ячейкам
for i in range(n - 1): #вызов для каждого предмета
    for j in range (n - 1 - i): #предполагаемое кол-во перестановок
        if sort[j][1] < sort[j + 1][1]: #сортировка по цене
            sort[j], sort[j + 1] = sort[j + 1],sort[j]
        if sort[j][1] == sort[j + 1][1] and sort[j][0] > sort[j + 1][0]: #сортировка по коду
            sort[j], sort[j + 1] = sort[j + 1],sort[j]
[print(i[0], i[1]) for i in sort] #вывод 