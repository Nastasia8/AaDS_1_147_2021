print('Введите сумму вклада: ', end='')
P = float(input())
I = 5
m = 15 

def func(n, S):
    while n<=1:
        S = P*((1+(I/100)/(m/12))**(m/(12*n)))
        n *= 2
    return round((S), 3)

print('Через год вклад будет = ', func(0.25, 0.0))
