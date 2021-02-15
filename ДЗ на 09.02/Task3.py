def Calculate(x,y, opnum):
    ops = {
    0: (x + y), #sum
    1: (x * y), #произвежение
    2: (x / y), #деление
    3: (x - y), #вычитание
    4: x ** y   #pow
}
    try:
        return ops[opnum]
    except KeyError:
        print("Такого не существует")
    except ZeroDivisionError:
        print("Недопустиая операция")


x = int(input("Введите x "))
y = int(input("Введите y "))
opnum = int(input("Введите номер операции "))
Calculate(x,y, opnum)
