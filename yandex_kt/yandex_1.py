def func(N):
    if N < 1 or N > 1000:
        return(0)
    else:
        mass = list(map(int, input().split(maxsplit = N)))
        k = 0
        n = 0
        while n < N - 1:
            m = 0
            while m < N - n - 1:
                if mass[m] > mass[m+1]:
                    mass[m], mass[m+1] = mass[m+1], mass[m]
                    print(*mass)
                    k = k + 1
                m = m + 1
            n = n + 1
        if k == 0:
            return(print(k))
        return(0)

N = int(input())
       
func(N)
