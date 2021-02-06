from math import *
print('Введите массу груза')
m=float(input())
print('Введите коэфф жесткости')
k=float(input())
T=2*pi*sqrt((m/k))
W=sqrt(k/m)
print('Период колебаний=' '%.2f' % T,'Циклическая частота=', W)
