from math import sqrt
x = int(input("Введите x\n"))
y = int(input("Введите y\n"))
z = int(input("Введите z\n"))
def calc(x,y,z):
    D = y**2-4*x*z
    if D < 0:
        print("Корней нет")
    elif D == 0:
        f1 = -y/(2*x)
        print(f1)
    elif D >= 0:
        f1 = (-y + sqrt(D))/(2*x)
        f2 = (-y - sqrt(D))/(2*x)
        print(f1,f2)
calc(x,y,z)