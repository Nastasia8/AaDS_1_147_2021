from math import sqrt


def D(x=1, y=0, z=0):
    if x != 0:
        D = y**2-4*x*z
        if D == 0:
            f1 = -y/(2*x)
            print("F1=", f1)
        elif D > 0:
            f1 = round((-y+sqrt(D))/(2*x), 4)
            f2 = round((-y-sqrt(D))/(2*x), 4)
            print("F1=", f1, "F2=", f2)
        else:
            print("No solution")
    else:
        print("Error")


x = float(input("Ввдите x: "))
y = float(input("Ввдите y: "))
z = float(input("Ввдите z: "))
D(x=x, z=z, y=y)
