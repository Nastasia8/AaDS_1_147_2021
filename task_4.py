print('Введите сумму вклада: ', end='')
P = float(input())
I = 15
m = 6
n = 1

def func(m, I, P, n):
    return round((P*((1+(I/100)/(m/12))**(m/(12*n)))), 3)

print('Через год вклад будет = ', func(P, I, m, n))
