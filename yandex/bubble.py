from random import randint

def func(N, mass):
    n = 0
    while n < N - 1:
        m = 0
        while m < N - n - 1:
            if mass[m] > mass[m+1]:
                mass[m], mass[m+1] = mass[m+1], mass[m]
            m = m + 1
        n = n + 1
    return(print(str(mass)))

mass =[]
N = 10
i = 0

while i < N:
    mass.append(randint(-30, 30))
    i = i + 1
    
print(str(mass))   
func(N, mass)
