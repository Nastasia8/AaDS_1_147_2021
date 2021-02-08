from math import pi, sqrt
print ('Введите коэффициент жесткости пружины: ', end='')
k = float(input())
print('Введите массу: ', end='')
m = float(input())

def func_1(Res):
    Res = sqrt(k/m)
    return(Res)

def func_2(Res):
    Res = 2*pi*sqrt(m/k)
    return(Res)

print('Циклическая частота: T = ', round(func_1(0), 3))
print('Период колебаний пружинного маятника W = ', round(func_2(0), 3))
