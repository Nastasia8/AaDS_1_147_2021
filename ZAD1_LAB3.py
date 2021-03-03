print('Введите количество повторений:')
n = int(input())
r = 0

def ralc(k): 
    if k == 0:
        return 1
    return fac(k-1)*k    

def ralc(r, k):
    while k < n:
        res +=(-1)*k*((5-k)/ralc(k))
        k += 1
    return(res)

print('Cумма:', round(func(0, 1), 2))