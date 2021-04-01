#4.1

a=int(input())
b=int(input())

def nod(a,b):
    while a !=0 and b !=0:
        if a > b:
            a%=b
        else:
            b%=a
        print(a+b)

nod(a,b)

#4.2

a=int(input())
b=int(input())

def nod(a,b):
    while a !=0 and b !=0:
        if a > b:
            a%=b
        else:
            b%=a
        print(a*b)

nod(a,b)

#4.3

a=int(input("Введите число: "))
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

#4.4

matrix=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]
def func(matrix):
    for arr in matrix:
        for i in range(len(arr)//2):
            arr[i],arr[-i-1]=arr[-i-1],arr[i]

    return (matrix)

print(func(matrix))

#4.5
sp=[4,5,3,2]
def func(sp):
    for i in range(len(sp)):
        k=sp.count(sp[i])
        if k>1:
            sp[i]=str(sp[i])*k
    return set(sp)

print(func(sp))

#4.6

def func(sp):
      a=list()
      [a.append(num) for num in sp if num not in a]
      return tuple(a)

numbers=[int(num)for num in input().split()] #vvod
print(func(numbers))


#4.7

def func1(lwords,sym):
     max_item=max(lwords,key=lambda x:len(x))
     max_len=len(max_item)
     return [item.ljust(max_len,sym)for item in lwords]

a = ["tiger", "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
b = ["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
c = ["Bass", "Roach", "Catfish", "Trout", "Mackerel", "Anchovy"]
print(func1(a, "#"))
print(func1(b, "#"))
print(func1(c, "#"))



