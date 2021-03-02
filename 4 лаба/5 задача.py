
sp=[2,3,4,2,3]
def fun(sp):
    for i in range(len(sp)):
        k=sp.count(sp[i])
        if k>1:
           sp[i]=str(sp[i])*l
        return set(sp)
fun(sp)

print(fun(sp))