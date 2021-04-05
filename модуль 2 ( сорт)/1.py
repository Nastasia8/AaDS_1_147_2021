i = int(input())
entermass = list(map(int, input().split()))[:i]



def buble_sort(mylist):
    sorts = 0
    last = len(mylist) - 1
    for x in range(0, last):
        for y in range(0, last - x):
            if mylist[y] > mylist[y + 1]:
                mylist[y], mylist[y + 1] = mylist[y + 1], mylist[y]
                for i in mylist:
                    sorts +=1
                    print(i, end=' ')

                print()
    if sorts == 0:
        print("0")


    return (mylist)


newlist = buble_sort(entermass).copy()


