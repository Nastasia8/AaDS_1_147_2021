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
