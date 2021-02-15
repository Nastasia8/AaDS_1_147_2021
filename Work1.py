# № задания указан в коментарии
# в данном файле находятся все задания 


#Задание 1
text ="Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected."
print ("p =", text.count('p'), '\n', "o=", text.count('o'))


#Задание 2
from math import sqrt, pi
print('Введите массу груза')
m=float(input())
print('Введите коэффициент жесткости пружины')
k=float(input())
def function():
    w=sqrt(k/m)
    T=2*pi*sqrt(m/k)
    print(w, '\n', T)
function()


#Задание 3
x=float(input("Введите число x" '\n'))
y=float(input("Введите число y" '\n'))
def function():
    summ = x+y
    com = x*y
    if (y!=0):
        div = x/y
    else:
        print("Ты CLOWN")
        div ="не существует" 
    sub = x-y
    power = x**y
    print (" Сумма =", summ, '\n', "Деление =", div , '\n', "Произведение =", com, '\n', "Разность =", sub , '\n', "Степень =", power, '\n')
function()


#Задание 4
P=120000
m=3
n=3
I=15
def summ():
    if (m==3 or m==6 or m==12):
        S=P*(1+((I/100)/(m/12))**(m/(12*n)))
        print("Сумма вклада будет =", S, "рублей.")
    else:
        print("Такого периода начисления процентного вознаграждения не существует")
summ()


#Задание 5
k = float(input("Введите число k \n"))
def sum(n=1):
    S=0
    while (n<=k):
        S=S+(2/((2*n+1)*(2*n+3)))
        n=n+1
    print("Сумма числового ряда =", S, '\n')
def com(n=1):
    C=1
    while (n<=k):
        C=C*((-1)**(n-1)+n)
        n=n+1
    print("Произведение числового ряда =", C, '\n')
sum()
com()


#Задание 6
a=int(input("Введите первое целочисленное число в диапозоне \n"))
b=int(input("Введите последнее целочисленное число в диапозоне \n"))
def f(a, b):
    res=0
    for i in range(a, b+1):
        if i%2==0:
            res+=i
    print("Сумма = ", res)
def k(a, b):
    kek=0
    while a<b+1:
        if a%2==0:
            kek+=a
        a+=1
    print("Сумма =", kek)
f(a,b)
k(a,b)


#Задание 7
from math import sqrt
x=float(input("Введите x: \n"))
y=float(input("Введите y: \n"))
z=float(input("Введите z: \n"))

def dis():
    D = y**2-4*x*z
    if D<0:
        print('Корней нет')
    elif (x!=0 and D==0):
        x1=((-y)/2*x)
        print("Дискриминант =", D, '\n', "Корень = ", x1)
    elif (x!=0 and D>0):
        x1=((-y+sqrt(D))/2*x)
        x2=((-y-sqrt(D))/2*x)
        print("Дискриминант =", D, '\n', "Первый корень = ", x1, '\n', "Второй корень= ", x2)
    else:
         print('x не должен принимать значение равное 0')
dis()


#Задание 8
a=input('Введите целое шестизначное число: \n')
com=1
for i in a:
    com*=int(i)
print("Произведение цифр =", com)


#Задание 9
a=[7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
sum=0
i=0
while i<len(a):
    if a[i]<0:
        sum+=a[i]
    i+=1
print (sum)


#Задание 10
y=float(input("Введите число y" '\n'))
z=float(input("Введите число z" '\n'))
q=list(range(1,21))
print(q)
for i in q:
    i-=1
    c=q[i]
    if c%2==1 or c%2==2:
        x=q[i]
        q[i]=x**y**z
print (q)