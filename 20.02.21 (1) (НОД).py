print ('Введите X: ')
x = int(input())
print ('Введите Y: ')
y = int(input())
def fun(x,y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    itog = x + y
    print('НОД: ',itog)
fun(x,y)

