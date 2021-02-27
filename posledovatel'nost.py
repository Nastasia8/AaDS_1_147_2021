def func(f):
    n = 2
    f[0] = 0
    f[1] = 3
    while n < 15:
        f[n] = f[n-1] + f[n-2]
        n += 1
    return(f)
    
print(func([0] * 15))