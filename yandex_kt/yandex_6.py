def enter():
    n = int(input())
    c = list(map(int, input().split(maxsplit = n - 1)))
    prov(n, c)
    k = int(input())
    p = list(map(int, input().split(maxsplit = k - 1)))
    prov(k, p)
    if 1 > n or n > 100 or 1 > k or k > 100000:
        return(0)
    func(n, c, k, p)

def prov(n, c):
    for i in range(0, n):
        if 1 > c[i] or c[i] > 100000:
            return(0)

def func(n, c, k, p):
    for i in range(1, n+1):
        for j in range(0, k):
            if p[j] == i:
                c[i-1] = c[i-1] - 1
        if c[i-1] < 0:
            print('yes')
        else:
            print('no')
        
enter()
