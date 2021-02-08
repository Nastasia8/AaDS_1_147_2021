from math import *

print('Введите коэффициенты для уравнения')
print('ax^2+bx+c=0:')
x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))

discr = y ** 2 - 4 * x * z

print("Дискриминант D = ", discr)

if discr > 0:
    kor1 = (-y + sqrt(discr)) / (2 * x)
    kor2 = (-y - sqrt(discr)) / (2 * x)
    print('x1 = ', kor1)
    print('x2 = ', kor2)
elif discr == 0:
    kor = -y / (2 * x)
    print('x', kor)
else:
    print('Корней нет')
