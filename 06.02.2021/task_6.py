def func(res):
    print('Введите первое число: ', end='')
    x = int(input())
    print('Введите последнее число: ', end='')
    y = int(input())
    while x <= y:
        if x % 2 == 0:
            res += x
            x += 2
        else:
            x += 1
    return(res)

print('Сумма четных = ', func(res = 0))
