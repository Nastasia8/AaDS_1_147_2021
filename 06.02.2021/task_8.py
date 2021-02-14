print('Введите шестизначное число: ', end='')
x = int(input())

def func(res):
    for i in str(x):
        res *= int(i)
    return(print('Произведение цифр этого числа = ', res))

if x > 99999 and x<1000000:
    func(1)
else:
    print('Число не является шестизначным')
