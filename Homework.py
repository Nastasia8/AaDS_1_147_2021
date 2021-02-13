#1

text = "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected."

n_p = 0
n_o = 0

for i in text:
    if i == 'p' or i == 'P':
        n_p += 1
    elif i == 'o' or i == 'O':
        n_o += 1

print(f"N: {n_p}, O: {n_o}")


#2

from math import *

choose = input("Enter A if you want to count cyclic frequency or B if you want to count oscillation period of the spring pendulum: ")

k = int(input("Enter stiffness coefficient: "))
m = int(input("Enter mass: "))

def cyclic_f(k,m):
    return sqrt(k/m)

def osc_p(k,m):
    return 2*pi*(sqrt(m/k))

if choose == 'a':
    answer = cyclic_f(k,m)
    print(answer)
elif choose == 'b':
    answer = osc_p(k,m)
    print(answer)
    
    
#3

#from math import *

x = int(input("Enter x : "))
y = int(input("Enter y : "))
n_operation = int(input("Enter the number of the operation: (There should be the list of them) "))

def calc(n_operation, x, y):
    try:
        if n_operation == 1:
            return x + y
        elif n_operation == 2:
            return x*y
        elif n_operation == 3:
            try:
                return x//y
            except ZeroDivisionError:
                return "You cant divide by zero"
        elif n_operation == 4:
            return x-y
        elif n_operation == 5:
            return pow(x,y)
    except type(n_operation) == str or type(x) == str or type(y) == str:
        return "Uncorrect type of var"
    
print(calc(n_operation, x, y))

#4

#from math import *

rub = int(input("Enter amount of rubles: "))
i = int(input("Enter interest rate: "))
m = int(input("Enter number of interest accruals per year: "))
n = int(input("Enter term of the deposit in years: "))

def cost_contr(rub, i, m, n):
    return rub * pow((1 + ((i//100)//(m//12))), m/12*n)

print(cost_contr(rub,i,m,n))

#5

k = int(input())

def summ(k):
    n = 1
    while n <= k:
        formula = 2/((2*n+1)*(2*n+3))
        print(formula)
    n += 1

def multiply(k):
    n = 1
    while n <= k:
        formula = pow(-1,n-1)+n
        print(formula)
    n += 1
    
#6

n_begg = int(input("initial value: "))
n_end = int(input("end value: "))
summ = 0

while n_begg <= n_end:
    if n_begg % 2 == 0:
        summ += n_begg
    n_begg += 1
    
print(summ)
    
#7

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

def discriminant(x,y,z):
    d = y**y - 4*x*z
    if d < 0:
        return "There is no root"
    elif d == 0:
        return -y/2*x
    else:
        f_1 = (-y + sqrt(d))/2*x
        f_2 = (y + sqrt(d))/2*x
        return [f_1, f_2]

print(discriminant(x,y,z))

#8.1

n = int(input())

def n_mult(n):
    
    multiply = 1
    
    if n // 100000 == 1:
        while n > 0:
            multiply *= n%10
            n //= 10
        return multiply

print(n_mult(n))

#8.2

n = input()
multiply = 1

for i in n:
    if len(n) == 6:
        multiply *= int(i)

print(multiply)

#9

a = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
index = 0
summ = 0

while index < len(a):
    if a[index] < 0: 
        summ += a[index]
    index += 1
    
print(summ)

#10

a = []
y = int(input())
z = int(input())

for i in range(1,21):
    a.append(i)
    
def pow(mas, y, z):
    for x in range(len(mas)):
        if a[x] % 2 == 1:
            a[x] = a[x]**(y**z)
    
    print(a)
    
print(pow(a,y,z))


            


        



        
    

    
    


    
    