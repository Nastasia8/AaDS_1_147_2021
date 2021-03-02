#задача4(a)
def func (matrix):
    for arr in matrix:
        for i in range(len(arr)//2):
            arr [i], arr [-i-1]=arr[-i-1],arr[i]
    return matrix
matrix = [[1,2,3,4,], [2,3,4,5,], [3,4,5,6]]



#задача4(b)
a = [[13, 97, 56], [17, 23, 85], [22, 45, 66]]

for num in range(len(a)):
    print(a[num])
print()
for num in range(len(a)):
    print(a[num][::-1])



#задача5
def func(sp):
    for i in range(len(sp)):
        k=sp.count(sp[i])
        if k>1:
            sp[i]=str(sp[i])*k
    return set(sp)

sp=[1, 7, 4, 7, 15, 4, 7, 5, 2]
print (func(sp))



#задача6
def func(sp):
    a=list()
    [a.append(num) for num in sorted(sp) if num not in a ]   #вводить через пробел список
    return tuple(a)

number =[int (num) for num in input().split()]
print(func(number))



#задача7
def fun1(lwords,sym):
    max_item= max(lwords,key=lambda x:len(x))
    max_len=len(max_item)
    return[item.ljust(max_len,sym) for item in lwords]

words1=["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
words2=["tiger", "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
words3=["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]

print(fun1(words1,"#"))
print(fun1(words2,"#"))
print(fun1(words3,"#"))