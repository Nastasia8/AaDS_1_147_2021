x = float(input("Введите x\n"))
y = float(input("Введите y\n"))
i = int(input("Введите номер операции\n"))

def calc (x,y,i):
    if i  == 1:
        print(x+y)
    if i == 2:
        print(x*y)
    if i ==3:
        if y == 0:
            print("Деление на 0")   
        else:
            print(x/y)
    if i==4:
        print(x-y)
    if i==5:
        print(x**y)
calc(x,y,i)
