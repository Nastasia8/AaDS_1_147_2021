a = int(input())
b = int(input())
c = input('')
def fun(a,b,c):
    if c == 'Сложение':
        print(a+b)
    if c == 'Вычитание':
        print(a-b)
    if c == 'Умножение':
        print(a*b)
    if c== 'Степень':
        print(a**b)
    if c == 'Деление':
        if b != 0:
        print(a/b)
    else:
        print('На 0 делить нельзя!')
fun(a,b,c)