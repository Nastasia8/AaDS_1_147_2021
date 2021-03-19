n=int(input())
array=[]
for i in range(n):
    key,value=map(int,input().split())
    array.append([key,value])

for i in range(len(array)):
    imax = i
    if array[imax][1] < array[i][1]:
        array[imax], array[i] = array[i], array[imax]
    elif array[imax][1] == array[i][1]:
        if array[imax][0] > array[i][0]:
            array[imax], array[i] = array[i], array[imax]
    
for l in range(n):
    print(array[l], end = " ")
