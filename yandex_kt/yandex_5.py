def check(mass):
    i = 0
    while i < len(mass):
        if mass[i] > 2 * 1000000000:
            return(0)
        else:
            return(print(len(mass)))
    
N = int(input())

if 1 <= N <= 100000: 
    mass = list(map(int, input().split(maxsplit = N - 1)))
    mass = list(set(mass))
    check(mass)
