#4.1 
print ('Введите X: ')
x = int(input())
print ('Введите Y: ')
y = int(input())
def fun(x,y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    itog = x + y
    print('НОД: ',itog)
fun(x,y)
#4.2
print ('Введите X: ')
x = int(input())
print ('Введите Y: ')
y = int(input())
def fun(x,y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    itog = x + y
    return itog
nok=(x*y)/fun(x,y)
print ('НОК: ',nok)
#4.3
x=int(input("Введите X: "))
def fun(x):
  while x!=1:
        if x%2==0:
            x=x//2
        else:
            x=x*3
            x=x+1
            x=x//2
        print(x, end=" ")

fun(x)
#4.4
matrix=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]
def func(matrix):
    for arg in matrix:
        for i in range(len(arg)//2):
            arg[i],arg[-i-1]=arg[-i-1],arg[i]

    return (matrix)

print(func(matrix))
#4.5
def func(sp):
    for i in range(len(sp)):
        k=sp.count(sp[i])
        if k>1:
            sp[i]=str(sp[i])*k
    return set(sp)
sp=[2,3,4,2,3]
print(func(sp))
#4.6
def func(sp):
      a=list()
      [a.append(num) for num in sp if num not in a]
      return tuple (a)
numbers=[int(num)for num in input( ).split()]
print(func(numbers))
#4.7
def func1(lwords,sym):
     max_item=max(lwords,key=lambda x:len(x))
     max_len=len(max_item)
     return [item.ljust(max_len,sym)for item in lwords]

words1 = ["tiger", "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
words2 = ["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
words3 = ["Bass", "Roach", "Catfish", "Trout", "Mackerel", "Anchovy"]
print(func1(words1, "#"))
print(func1(words2, "#"))
print(func1(words3, "#"))