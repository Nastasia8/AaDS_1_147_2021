a = int(input("Введите число: "))


def func(a):
    while a > 0:
        if a % 2:
            print(a / 2)
            return
        else:
            print(((a*3)+1)/2)
            return
    else:
        print('Что-то тут не так')


func(a)
