  
def funk():
    m=0
    n = 1
    if (m >= 100000 or m < 1000000):
        for i in range(0, 6):
            n *= m % 10
            m = m // 10
    else:
        print("Ошибка")
    return n


m = int(input("Введите число: "))
print(funk())