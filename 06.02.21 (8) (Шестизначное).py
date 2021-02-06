print('Введите шестизначное число: ')
x = int(input())

def func(itog):
    for i in str(x):
        itog *= int(i)
    return(print('Произведение цифр этого числа = ', itog))

if x > 99999 and x<1000000:
    func(1)
else:
    print('Ошибка')
