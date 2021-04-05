x = int(input("Введите x\n"))
y = int(input("Введите y\n"))
def nod(x,y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    print("Нод:",x + y)

nod(x,y)