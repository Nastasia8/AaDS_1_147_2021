print('Введите нужное количество элементов и сами эелементы. После введенего элемента нажмите  Enter')
entermass = []
n = int(input())
for i in range(n):
    entermass.append(int(input()))
print(entermass)

def buble_sort(mylist):
    last = len(mylist) - 1
    for x in range(0,last):
        for y in range(0,last-x):
            print(mylist)
            if mylist[y] > mylist[y+1]:
                mylist[y], mylist [y+1] = mylist [y+1], mylist[y]
    return mylist

print('Старый список: ', entermass)
newlist = buble_sort(entermass).copy()
print('Новый список: ', newlist)