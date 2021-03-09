
x = int(input("Введите x\n"))
y = int(input("введите y\n"))

def nod(x,y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return(x+y)

def nok(x,y):
    a = (x*y)/(nod(x,y))
    print("НОК:",int(a))

x = int(input("Введите x\n"))
y = int(input("введите y\n"))

nok(x,y)