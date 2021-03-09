import re

i = int(input())
raw = input()
entermass = [int(i) for i in raw.split(' ') if i.isdigit()]



def buble_sort(mylist):
    last = len(mylist) - 1
    for x in range(0,last):
        for y in range(0,last-x):
            for i in mylist:
                print(i, end = ' ')
            print()
            if mylist[y] > mylist[y+1]:
                mylist[y], mylist [y+1] = mylist [y+1], mylist[y]
    return mylist

newlist = buble_sort(entermass).copy()
for i in newlist:
    print(i, end = ' ')