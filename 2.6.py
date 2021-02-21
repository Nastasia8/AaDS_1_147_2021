def counter(num):
    Sum = 0
    multy = 1
    for i in num:
        Sum += i
        multy *= i
    print('Сумма:', Sum, '\nПроизведение:', multy)

num = {1, 2, 3, 4, 5}
counter(num)
