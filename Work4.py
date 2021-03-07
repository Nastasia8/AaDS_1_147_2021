# № задания указан в коментарии
# в данном файле находятся все задания 


#Задание 1
def NOD(a=int(input("Введите первое натуральное число\n")), b=int(input("Введите второе натуральное число\n"))):
    if a>0 and b>0:
        while a!=0 and b!=0:
            if a>b:
                a=a%b
            else:
                b=b%a
        print("Наибольший общий делитель -", a+b)
    else:
        print("Введите натуральные числа")
NOD()


#Задание 2
from math import gcd
def NOK(a=int(input("Введите первое натуральное число\n")), b=int(input("Введите второе натуральное число\n"))):
    if a>0 and b>0:
        while a!=0 and b!=0:
            print("Наименьшее общее кратное -", ((a*b)//gcd(a,b)))
            break
    else:
        print("Введите натуральные числа")
NOK()


#Задание 3
b=[]
def reducibility(a=int(input("Введите натуральное число\n"))):
    if a>0:
        b.append(a)
        while a!=1 and a>0:
            if a%2==0:
                a=a/2
                b.append(a)
            else:
                a=a*3+1
                b.append(a)
        print (b)
    else:
        print("Введите натуральное числа")
reducibility()

#Задание 4

from random import randint
N=int(input("Введите длину матрицы \n"))
M=int(input("Введите ширину матрицы \n"))
print('\n')
m = ([[randint(-100,100) for j in range(N)] for i in range(M)])
print(m, '\n')

print(m[::-1])

def func(matrix):
    for x in matrix:
        for i in range(len(x)//2):
            x[i],x[-i-1]=x[-i-1],x[i]
    print(matrix)
func(m)

#Задание 5
l=[1, 7, 4, 7, 15, 4, 7, 5, 2]

def func(l):
    for i in range(len(l)):
        k=l.count(l[i])
        if k>1:
            l[i]=str(l[i])*k
    return set(l)

print(func(l))


#Задание 6
nums=[int(x) for x in input().split()]

def func(nums):
    a=list()
    for x in sorted(nums):
        if x not in a:
            a.append(x)
    return(tuple(a))

print(func(nums))


#Задание 7
def func(lwords, sym):
    max_i=max(lwords, key=lambda x:len(x))
    max_l=len(max_i)
    return([item.ljust(max_l,sym) for item in lwords])

list1=["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
list2=["tiger",  "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
list3=["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]
print(func(list1, "@"),'\n',func(list2, "$"),'\n',func(list3, "&"))
