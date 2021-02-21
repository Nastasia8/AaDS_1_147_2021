def func(a):
    if a>1:
        p=1
        for n in range(1, a+1):
            p=p*((n+(3**n))/(n+(5**(2*n))))
        print("Прозведение числового ряда равно:", p)
    else:
        print("A должно быть больше 1!")
k=int(input("Введите число:"))
func(k)