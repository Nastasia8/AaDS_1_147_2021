#задача1
def NOD(x, y):
    while y:
        x, y = y, x % y
    return x
x = int(input("введите значение x:"))
y = int(input("введите значение y:"))

print ("НОД =", NOD(x, y))
#задача2

def HOK(a,b):
    a1= a
    b1= b
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a1*b1//(a+b)

a = int(input('Input 1 number:'))
b = int(input('Input 2 number:'))
print("HOK({0};{1}) = {2}".format(a,b, HOK(a, b)))


#задача3

a=int(input(""))

def func(a):

  while a!=1:
        if a%2==0:
            a=a//2
        else:
            a=a*3
            a=a+1
            a=a//2
        print(a, end=" ")

func(a)


#Задача4

matrix = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
def func(matrix):
    for arr in matrix:
        for i in range(len(arr)//2):
            arr[i],arr[-i-1]=arr[-i-1],arr[i]
    return(matrix)
func(matrix)
print(matrix)

#Задача5
def func(sp):
    for i in range(len(sp)):
        k=sp.count(sp[i])
        if k>1:
            sp[i]=str(sp[i])*k
    return set(sp)

sp=[2,3,4,2,3]

print(func(sp))

#Задача6
sp = [1,2,1,5,6]
def func(sp):
    a = list()
    [a.append(num)  for num in sp if num not in a ]
    return tuple(a)


numbers = [int(num)for num in input().split()] 

print(func (numbers))


#Задача7


def func(lwords,sym):

    max_item=max(lwords,key = lambda x:len(x))
    max_len=len(max_item)
    return[item.ljust(max_len,sym) for item in lwords]


words1 = ["tiger","leopard","elephant"]
words2 = ["tiger",  "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
words3 = ["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]


print(func(words1,"#"))
print(func(words2,"#")) 
print(func(words3,"#"))
