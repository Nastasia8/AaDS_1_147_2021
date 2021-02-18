# № задания указан в коментарии
# в данном файле находятся все задания 


#Задание 1
n=int(input("Введите n \n"))
import math
S,k = 0, 0
def Sum(k,S):
    while k<=n:
        k+=1
        S+=(-1)*k*(5-k)/math.factorial(k)
    print("Сумма ряда =", round(S, 3))
Sum(k,S)


#Задание 2
def fib(n=15):
    x,y=1,3
    for i in range(n):
        x, y=y, x+y
        print(y)
fib()


#Задание 2(альтернативное решение)
def fib(i):
    if i==0:
        return 1
    elif i==1:
        return 3
    else:
        return fib(i-1)+fib(i-2)
def main(fib):
    n=0
    while n>=0 and n<=15:
        n+=1
        i = fib(n)
        print (i)
main(fib)


#Задание 3
text=["Crime and Punishment", 1, 331, 1866, "The Master and Margarita", 1, 470, 1966, "War and Peace", 4, 1274, 1869, "And Quiet Flows the Don", 4, 1600, 1940]
dict={}
def key(text):
    for x in text:
        if type(x) == str:
           dict[x]=1
def val(dict):
    dict["Crime and Punishment"] = text[1:4]
    dict["The Master and Margarita"] = text[5:8]
    dict["War and Peace"] = text[9:12]
    dict["And Quiet Flows the Don"] = text[13:15]
    print (dict)
key(text)
val(dict)


#Задание 4
a=["Bass", "Pike", "Roach", "Catfish", "Trout", "Mackerel", "Salmon", "Zander", "Anchovy"]
print(a)
def sortByAlphabet(inputStr):
        return inputStr[-1]
b = sorted(a, key=sortByAlphabet)
print(b)
x = ' '.join(b)
print(x)
for word in list(x.split()):
    print(' '.join(list(word[-1])))


#Задание 5
a=[14, 46, 10, -78, 0, 6, -31, -24, 56, 17, -83, -4]
dict = {}
for i in a:
    if i > 0:
       dict[i]="positive"
    elif i < 0:
       dict[i]="negative"
    else:
       dict[i]="zero"
print(dict)