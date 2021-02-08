#задача1
a= "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected."
s=0
k=0

for i  in a:
	if i == "o":
		s+=1
		
for i  in a:
	if i == "p":
		k=k+1

print ("количество o:", s,"количество p:",k)




#задача2
from math import sqrt,pi
T=0
W=0

m = int(input())
k = int(input())

T = 2* pi * sqrt(m/k)
W=1/T

print("период колебаний пружинного маятника:",T,"циклическая частота:",W)




#задача3
x = int(input("Введите x: "))
y = int(input("Введите y: "))
print ("выберите операцию из списка:\n","сложение-1\n", "умножение-2\n","деление-3\n","вычитание-4\n","возведение в степень-5\n")
n=int(input("Введите номер операции: "))

S=0
P=0
D=0
V=0
W=0

S=x+y
P=x*y
D=x/y
V=x-y
W=x**y

if n==3 :
	if y!=0:
		print(D)
	else:
	    print("ввод некорректных данных. на ноль делить нельзя")
if n==1:
	print(S)
if n==2:
	print(P)
if n==4:
	print(V)
if n==5:
	print(W)
if n>5:
	print("ввод некорректных данных. выберите номер в диапозоне от 1 до 5")




#задача4 "Напишите задание пожалуйста на русском языке, не понятно что нужно было делать!"



#задача5
k = int(input("Введите k (колличество повторений): "))
rezultat = 0

def func_proizvedenie(rezultat, n):
    while n < k:
        rezultat = rezultat + 2/((2*n+1)*(2*n+3))
        n = n+ 1
    return(rezultat)

def func_symma(rezultat, n):
    while n < k:
        rezultat = rezultat * (-1)**(n-1)+n
        n = n + 1
    return(rezultat)

print("Сумма числового ряда = ", round(func_proizvedenie (0, 1), 2), "\n", "Произведение числового ряда = ", round(func_symma(1, 1), 2))



#задача6(для цикла for)
n = int(input("Введите начало диапазона: "))
f = int(input("Введите конец диапазона: "))
S=0

for x in range(n,f+1):
	if x%2==0:   
			S=S+x

print("сумма чётных чисел: ",S)


#задача6 (для цикла while)
n = int(input("Введите начало диапазона: "))
f = int(input("Введите конец диапазона: "))
S=0

while n<=f:
	if n%2==0:
			S=S+n
			n+=1
	else:
		n+=1

print("сумма чётных чисел: ",S)




#задача7
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

D=0
f=0
f1=0
f2=0

D=y*y - 4*x*z
f=-y/2*x
f1=(-y + D**0.5) / (2 * x)
f2=(-y - D**0.5)/ (2 * x)

if D<0:
	print("корней нет")
if D==0:
	print(f)
if D>0:
	print(f1,f2)




#задача8
num = int(input("Введите шестизначное число: "))
pro = 1

if num<1000000 and num>99999:
    while (num != 0):
        pro = pro * (num % 10)
        num = num // 10
    print("Произведение цифр числа равно: ", pro)
else:
    print("число не шестизначное!")




#задача9
spisok = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
So=0
i=0
while i < len(spisok):
		if spisok[i]<0:
			So=So+spisok[i]
		i+=1
print("Сумма отрицательных чисел: ", So)




#задача10 
y = int(input("Введите y: "))
z = int(input("Введите z: "))

P=0

for x in range(1,21,2):
		P=x**y**z
		print(P, end=",")







































