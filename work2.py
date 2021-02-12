# № задания указан в коментарии
# в данном файле находятся все задания 


#Задание 1
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
c=[]
for b in a:
    if (b)%2==0:
        c.append(b)
print(c)

print([d for d in a if d%2==0])

def strainer(i):
    return i%2==0
print(list(filter(strainer,a)))

print(list(filter(lambda k: k%2==0, a)))


#Задание 2
animals=["tiger", "leopard", "elephant", "fox", "wolf", "camel", "raccoon"]
animals[0],animals[-1] = animals[-1],animals[0]
print(animals)


#Задание 3
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
b=[3, 9, 2, 1, 8, 7, 4, 10, 6]
def TF(a=set(), b=[]):
    if a==b:
        return True
    else:
        return False
print (TF(b,a))


#Задание 4
a=(1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
b=[]
for i in range (len(a)):
    if a[i]==2:
        b.append(i)
print (b)


#Задание 5
text="Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower().split()
dict={}
for a in text:
    if a in dict:
        dict[a]+=1
    else:
        dict[a]=1
print(dict)


#Задание 6
#Многовероятно я не понял задание
x=list(input("Введите набор целых чисел через запятую \n").lower().split(', '))
d={}
for i in x:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
def summ():
    print("сумма элементов словаря =", sum(d.values()))
summ()

import functools
def com():
    print ("произведение элементов словаря =", functools.reduce(lambda a, b : a * b, d.values())) 
com()


#Задание 7
from random import randint
x=int(input("Введите длину стороны квадратной матрицы \n"))
print('\n')
m = ([[randint(-100,100) for j in range(x)] for i in range(x)])    # randint - заполнение массива значениями
def printMatrix (m): 
   for row in m: 
      for x in row: 
          print ( "{:4d}".format(x), end = " " )                # "{:4d}".format(x) - всего лишь целочисленное форматирование
      print ()
printMatrix(m)

def idn(m):
    print('\n')
    i=0
    for k in range(len(m)):
        m[k+i][-k-i-1]*=2
    i+=1
    for row in m: 
      for x in row: 
          print ( "{:4d}".format(x), end = " ") 
      print ()
idn(m)

"""
#Задание 8                     #оно устало, его не трогать
a=(1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)
x=int(input("Введите целочисленное число \n"))
def gl(a, x):
    if x in a:
        k=1
        l=0
        while a[k]!=x and a[l]!=x:
            k+=1
            l-=1
        print(a[k:l+1])
    else: 
        print("The tuple doesn't contain a character =", x)
gl(a,x)
"""