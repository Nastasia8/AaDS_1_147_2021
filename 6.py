spis = []
n = 2
while n:
    for i in range(n):
        k = int(input('Введите число:'))
        spis.append(k)

    summ = 0
    for i in range(spis[0], spis[1]+1):
        if i % 2 == 0:
            summ += i
    print(summ)
    break
print('Завершение')
