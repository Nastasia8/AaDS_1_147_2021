def ByCycle(st, fin):
    counter = 0
    for i in range(st,fin+1):
        if i%2 == 0:
            counter+=1
    return counter

def ByWhile(st, fin):
    counter = 0
    while st <= fin:
        if st%2 == 0:
            counter+=1
        st+=1
    return counter

start = int(input("Укажите начало диапазона: \n"))
fin = int(input("Укажите конец диаппазона: \n"))
print(ByCycle(start, fin))
print(ByWhile(start, fin))