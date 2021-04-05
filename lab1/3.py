def calc ():
    x = float(input("Введите x\n"))
    y = float(input("Введите y\n"))
    i = int(input("Введите номер операции\n"))
    if i  == 1:
        print(x+y)
    if i == 2:
        print(x*y)
    if i ==3:
        print(x/y)
    if i==4:
        print(x-y)
    if i==5:
        print(x**y)
calc()
