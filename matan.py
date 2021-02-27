from math import sqrt

print('x')
x = float(input())
print('y')
y = float(input())
print('z')
z = float(input())

def func(x, y, z):
    D = y*y - 4*x*z
    if D < 0:
        print('net korn9')
    elif D == 0:
        print(round(((-y)/(2*x)), 3))
    else:
        print(round((((-y)+sqrt(D))/(2*x)), 3), round(((-y)-sqrt(D))/(2*x)), 3)
func(x, y, z)
