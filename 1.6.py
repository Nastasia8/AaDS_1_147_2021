def Solution(x1=0, x2=10):
    summ = 0
    for n in range(x1, x2+1, 1):
        if (n % 2) == 0:
            summ += n
    return summ


x1 = int(input("Ввдите начало диапозона: "))
x2 = int(input("Ввдите конец диапозона: "))
print(Solution(x1=x1, x2=x2))
