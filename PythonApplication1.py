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




#задача6
a = int(input("Первое число: "))
b = int(input("Последнее число: "))
s=0

for n in range(a,b+1):
	if n%2==0:   
			s=s+n

print("сумма чётных чисел равна ",s)





#задача7
from math import sqrt
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

D=0
f=0
f1=0
f2=0

D=y*y - 4*x*z
f=-y/2*x
f1=(-y + sqrt(D)) / (2 * x)
f2=(-y - sqrt(D))/ (2 * x)

if D<0:
	print("корней нет")
if D==0:
	print(f)
if D>0:
	print(f1,f2)




#задача8
a = int(input("Введите шестизначное число: "))
P = 1

if a>99999 and a<1000000:
    while (a != 0):
        P = P * (a % 10)
        a = a // 10
    print("Произведение цифр числа равно: ", P)
else:
    print("Это не шестизначное число.")



#задача 9
a=[7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
s=0
while n<0:
	s=s+n
print("сумма отрицательных чисел равна ",s)




#задача10 
y = int(input("Y:"))
z = int(input("Z:"))
P=0

for x in range(1,21):
	P=x**y**z
	print(P)
