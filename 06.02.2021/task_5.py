print('Введите колличество повторений: ', end='')
k = int(input())
res = 0

def func_1(res, n):
    while n < k:
        res += 2/((2*n+1)*(2*n+3))
        n += 1
    return(res)

def func_2(res, n):
    while n < k:
        res *= (-1)**(n-1)+n
        n += 1
    return(res)

print('Сумма = ', round(func_1(0, 1), 3))
print('Произведение = ', round(func_2(1, 1), 3))
