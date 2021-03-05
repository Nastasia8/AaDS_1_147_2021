#задача4
#def func (matrix):
#    for arr in matrix:
#        for i in range(len(arr)//2):
#            arr [i], arr [-i-1]=arr[-i-1],arr[i]
#    return matrix
#matrix = [[1,2,3,4,], [2,3,4,5,], [3,4,5,6]]



#задача5
#def func(sp):
#    for i in range(len(sp)):
#        k=sp.count(sp[i])
#        if k>1:
#            sp[i]=str(sp[i])*k
#    return set(sp)

#sp=[1, 7, 4, 7, 15, 4, 7, 5, 2]
#print (func(sp))


#задача6
#def func (sp):
#    a=list()
#    [a.append(num) for num in sorted(sp) if num not in a]
#    return tuple(a)

#numbers = [int(num) for num in input().split()]
#print (func(numbers))


#задача7
#def func(lwords,simb):
#    max_item = max(lwords, key=lambda x:len(x))
#    max_len = len(max_item)
#    return [item.ljust(max_len,simb)  for item in lwords]


#words1 = ["tiger",  "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]
#words2 = ["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
#words3 = ["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]
#print(func(words1, "#"))
#print(func(words2, "#"))
#print(func(words3, "#"))

