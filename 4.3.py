list = []
def Func():
    a = int(input('Введите число:'))
    while a > 1:
        if a % 2 == 0:
            a = a / 2
            list.append(a)
        elif a % 2 != 0:
            a = (a * 3 + 1) / 2
            list.append(a)
    return a, list 

print(Func())               