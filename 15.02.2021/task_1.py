print('Введите колличество повторений (n): ', end='')
n = int(input())

def summa(n):
    k = 1
    Sum = 0
    while k <= n:
        Sum += (-1)*k*((5 - k)/factorial(k))
        k += 1
    return(Sum)

def factorial(k):
    if k > 1:
        return k*factorial(k - 1) 
    return(k)

print(round(summa(n), 3))
