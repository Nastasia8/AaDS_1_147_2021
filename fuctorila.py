print('povtorit')
n = int(input())

def summa(n):
    k = 1
    Suma = 0
    while k <= n:
        Suma += (-1)*k*((5 - k)/factorial(k))
        k += 1
    return(Suma)

def factorial(k):
    if k > 1:
        return k*factorial(k - 1) 
    return(k)

print(round(summa(n), 3))