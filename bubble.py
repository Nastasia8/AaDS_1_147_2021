N = int (input ("Введите количество элементов в массиве: "))
a = [int(num) for num in input("Введите массив: ").split()]

if N<1 or N>1000:
    print ("Ошибка")
else:
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                print(a)
            else:
                print(0)
