from random import randint

def func(N, mass):
    n = 0
    k = 0
    while n < N - 1:
        m = 0
        while m < N - n - 1:
            if mass[m] > mass[m+1]:
                k = k + 1
                mass[m], mass[m+1] = mass[m+1], mass[m]
            m = m + 1
        n = n + 1
    return(print(k))

mass =[]
N = int(input())
i = 0

while i < N:
    mass.append(randint(-30, 30))
    i = i + 1
       
func(N, mass)
