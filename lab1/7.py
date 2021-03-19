from math import sqrt
def main():
    x = int(input("Введите x\n"))
    y = int(input("Введите y\n"))
    z = int(input("Введите z\n"))
    calc(x, y, z)


def calc(x, y, z):
     D = y**2-4*x*z
     if D < 0:
        print("Корней нет")
     if D == 0:
        f1 = -y/(2*x)
        print(f1)
     if D >= 0:
        f1 = (-y + sqrt(D))/(2*x)
        f2 = (-y - sqrt(D))/(2*x)
        print(round(f1, 3),round(f2, 3))


main()
