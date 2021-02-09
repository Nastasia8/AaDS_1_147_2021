#1 способ
def fan(list_a):
    new_list=[]
    for number in list_a:
        if number%2==0:
            new_list.append(number)
    print (new_list)
    
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
fan(a)
#2 способ
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
print ([num for num in a if num %2==0])
#3 способ
def fun(number):
    return number %2==0
a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
print (list(filter(fun,a)))
#4 способ
def fun(number):
    return number %2==0
a=list(range(1,11))
print (list(filter(lambda number:number%2==0,a)))

