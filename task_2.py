from math import *
print ('Введите коэффициент жесткости пружины: ', end='')
k = float(input())
print('Введите массу: ', end='')
m = float(input())
print('Циклическая частота: T = ', round(sqrt(k/m), 3))
print('Период колебаний пружинного маятника W = ', round(2*pi*(m/k), 3))
