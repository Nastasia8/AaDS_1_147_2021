#№1
x1=int(input())
y1=int(input())
def nod(x,y):
    a=x
    b=y
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x
    print("НОД({}; {}) = {}".format(a,b,y))
nod(x1,y1)

#№2
x1=int(input())
y1=int(input())
def nok(x,y):
    nk=1
    while nk%x!=0 or nk%y!=0:
        nk+=1
    print("НОК({}; {}) = {}".format(x,y,nk))
    return nk
print(nok(x1,y1))

#№3
def f(a):
    print(a,"->")
    m=[]
    while a!=1:
        if a%2==0:
            a=a/2
        else:
            a=(a*3+1)/2
        m.append(a)
    print(m)
    print(a)
x=int(input())
f(x)

#№4.a
from random import randint
n=int(input())#строки
m=int(input())#столбцы
a= [[randint(10,99) for j in range (m)] for i in range (n)]
for i in range (n):
    print (a[i])
print()
for j in range (m//2):
    for i in range (n):
        a[i][j],a[i][m-j-1]=a[i][m-j-1],a[i][j]
for i in range(n):
    print(a[i])

#№4.b
from random import randint
n=int(input())#строки
m=int(input())#столбцы
a= [[randint(10,99) for j in range (m)] for i in range (n)]
for i in range (n):
    print (a[i])
print()
for i in range (n//2):
    for j in range (m):
        a[i][j],a[n-i-1][j]=a[n-i-1][j],a[i][j]
for i in range(n):
    print(a[i])

#№5
def cre(sp):
    a=set()
    for i in range (len(sp)):
        if sp[i] in a:
            k=0
            for j in range(0,i+1):
                if sp[j]==sp[i]:
                    k+=1
            a.add(str(sp[i])*k)
        else:
            a.add(sp[i])
    return a
spisok=[1, 7, 4, 7, 15, 4, 7, 5, 2]
print(cre(spisok))

#№6
def ha(sp):
    a=set(sp)
    
    s=list(a)
    s.sort()

    t=tuple(s)
    return(t)
spis=[int(input()) for i in range (int(input ()))]
print(ha(spis))
