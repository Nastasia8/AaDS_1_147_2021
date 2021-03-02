def func(sp):
    for i in range(len(sp)):
        k=sp.count(sp[i])
        if k>1:
            sp[i]=str(sp[i])*k
    return set(sp)
sp=[2,3,4,2,3]
print(func(sp))
    
