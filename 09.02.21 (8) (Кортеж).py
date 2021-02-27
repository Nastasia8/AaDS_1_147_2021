num=(1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)
print ('Введите значение элемента: ')
x=float(input())
def fun(num,x):
    if x in num:
        start=num.index(x)
        k=num.count(x)
        if k>1:
            i=1
            end=start
            while i<k:
                end=num.index(x,end+1)
                i+=1
            print (num[start:end+1])
        else:
            print (num[start:])
    else:
        print('x не входит')
fun(num,x)
