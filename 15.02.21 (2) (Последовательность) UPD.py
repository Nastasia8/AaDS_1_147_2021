#1 способ
def func(p):
    p[0]=0
    p[1]=3
    n=2
    while n<15:
        p[n]=p[n-1]+p[n-2]
        n+=1
    return(p)

print(func([0] * 15))
#2 способ
def func1(n):
    if n==0:
        return 0
    elif n==1:
        return 3
    else:
        return func1(n-1)+func1(n-2)
def func2(func1):
    p=0
    while p>=0 and p<=14:
      print (func1(p), end= ", ")
      p+=1
func2(func1)
