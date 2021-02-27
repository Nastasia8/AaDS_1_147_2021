def func(p):
    p[0]=0
    p[1]=3
    n=2
    while n<15:
        p[n]=p[n-1]+p[n-2]
        n+=1
    return(p)

print(func([0] * 15))
