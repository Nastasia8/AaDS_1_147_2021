from math import sqrt
def calc():
    x = int(input("Введите x\n"))
    y = int(input("Введите y\n"))
    z = int(input("Введите z\n"))
    D = y**2-4*x*z
    if D < 0:
        print("Корней нет")
    if D == 0:
        f1 = -y/(2*x)
        print(f1)
    if D >= 0:
        f1 = (-y + sqrt(D))/(2*x)
        f2 = (-y - sqrt(D))/(2*x)
        print(f1,f2)
calc()