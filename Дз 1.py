#1.1
p=0
o=0
for i in 'Python is an interpreted, high-level and general-purpose programming language. Pythons design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected.'.lower():
    if i == "p":
        p += 1
    if i == "o":
        o += 1
print ("p=",p,"o=",o)
#1.3
from math import *
print ('Введите Х')
x=float(input())
print ('Введите Y')
y=float(input())

operation =(input("Укажите операции (+,-,/,*,^): "))
 
if operation == "+":
    sum = round(x+y, 2)
    print("Сумма чисел",sum)
elif operation == "-":
    vch = round(x-y, 2)
    print("Вычитание",vch)
elif operation == "/":
    if (y==0):
        print ("Ошибка")
    else:
        delenie = round(x/y, 2)
    print("Деление",delenie)
elif operation == "*":
    umnoz = round(x*y, 2)
    print("Умножение",umnoz)
elif operation == "**":
    step = round(x**y, 2)
    print("Степень",step)
else:
    y = 0
    print("Ошибка")
#1.4
def calc(m):
    i = 15
    p = 100000
    n = 10
    s=p*(1+((i/100)/(m/12))**(m/(12*n)))
    print(s)

calc(3)
calc(6)
calc(12)
#1.5
print('Введите колличество повторений: ')
k = int(input())
res = 0

def func_1(res, n):
    while n < k:
        res += 2/((2*n+1)*(2*n+3))
        n += 1
    return(res)

def func_2(res, n):
    while n < k:
        res *= (-1)**(n-1)+n
        n += 1
    return(res)

print('Сумма = ', round(func_1(0, 1), 2))
print('Произведение = ', round(func_2(1, 1), 2))
#1.6
spis = []
n = 2
while n:
    for i in range(n):
        k = int(input('Введите число:'))
        spis.append(k)

    summ = 0
    for i in range(spis[0], spis[1]+1):
        if i % 2 == 0:
            summ += i
    print(summ)
    break
print('Завершение')
#1.7
from math import *

print('Введите коэффициенты для уравнения')
print('ax^2+bx+c=0:')
x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))

discr = y ** 2 - 4 * x * z

print("Дискриминант D = ", discr)

if discr > 0:
    kor1 = (-y + sqrt(discr)) / (2 * x)
    kor2 = (-y - sqrt(discr)) / (2 * x)
    print('x1 = ', kor1)
    print('x2 = ', kor2)
elif discr == 0:
    kor = -y / (2 * x)
    print('x', kor)
else:
    print('Корней нет')
#1.8
n = int(input('Введите число: '))
mult = 1
d = n
k = 1
while d // 10 > 0:
    k += 1
    d = d // 10
if k == 6:
    while n > 0:
        digit = n % 10
        mult = mult * digit
        n = n // 10
    print("Произведение:", mult)
print("Количество цифр:", k)
if k != 6:
    print("Ошибка")
#1.9
spisok = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
summ = 0
while spisok != []:
    if spisok[0] < 0:
        summ += spisok[0]
    del spisok[0]
print(summ)
#1.10
spis = [1, 20]
step1 = int(input("Первая степень: "))
step2 = int(input("Вторая степень: "))
spisupd = []


def inc(spis, step1, step2, spisupd):
    for i in range(spis[0], spis[1]):
        if i % 2 != 0:
            j = ((i ** step1) ** step2)
            spisupd.append(j)
    return spisupd


print(inc(spis, step1, step2, spisupd))