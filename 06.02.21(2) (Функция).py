#update
from math import *
def func1(m,k):
    T=2*pi*sqrt((m/k))
    return (T)

def func2(m,k):
    W=sqrt(k/m)
    return (W)

print('Введите массу груза')
m=float(input())
print('Введите коэфф жесткости')
k=float(input())
print('Период колебаний=',round(func1(m,k),2))
print('Циклическая частота=',round(func2(m,k),2))
