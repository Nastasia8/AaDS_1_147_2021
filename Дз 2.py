#2.4
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
#2.6
ad = {1, 2, 3, 4, 5}


def counter(ad):
    summ = 0
    comp = 1
    for i in ad:
        summ += i
        comp *= i
    print('Сумма:', summ, '\nПроизведение:', comp)


counter(ad)
#2.7
m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def diag(m):
    print("Матрица до преобразования")
    for i in range(len(m)):
        print(m[i])
    for i in range(len(m)):
        m[i][-i-1] *= 2
    print('Матрица после преобразования')
    for i in range(len(m)):
        print(m[i])


diag(m)
#2.8
a = int(input())
tuple = (1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)


def counter(tuple, a):

    if a not in tuple:
        print("The tuple doesn't contain a character = ", a)
    if a in tuple:
        ind = 0
        first_ind = float("inf")
        last_ind = 0
        for i in tuple:
            ind += 1
            if a == i:
                last_ind = ind
                if first_ind > ind:
                    first_ind = ind
        if first_ind == last_ind:
            print(tuple[first_ind - 1:])
        else:
            print(tuple[first_ind - 1:last_ind])
        print(first_ind, last_ind)


counter(tuple, a)


