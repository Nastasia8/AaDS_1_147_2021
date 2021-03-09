Results=[]  

def f(n):
    if n==0:
        a=0
    elif n==1:
        a=3
    else:
        a=f(n-1)+f(n-2)
    Results.append(a)    
    return a
f(6)
for i in range(15):
    print(Results[i],end=" ")