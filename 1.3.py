def summ(x, y):
    return x+y


def com(x, y):
    return x*y


def deff(x, y):
    if y == 0:
        print("Ввод некорректных данных")
    return x/y


def minus(x, y):
    return x-y


def stepen(x, y):
    return x**y


x = float(input("Enter x:"))
y = float(input("Enter y:"))
z = int(input("Chose operation:"))

if z == 1:
    print(summ(x, y))
elif z == 2:
    print(com(x, y))
elif z == 3:
    print(deff(x, y))
elif z == 4:
    print(minus(x, y))
elif z == 5:
    print(stepen(x, y))
