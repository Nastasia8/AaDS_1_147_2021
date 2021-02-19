print('Введите количество повторений:')
n = int(input())
res = 0


def fac(k):
    if k == 0:
        return 1
    return fac(k-1)*k


def func(res, k):
    while k < n:
        res += (-1)*k*((5-k)/fac(k))
        k += 1
    return(res)


print('Cумма:', round(func(0, 1), 2))
