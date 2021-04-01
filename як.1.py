def func(array):
    d=0
    for i in range(N-1):
         for x in range(N-i-1):
             if array[x] > array[x+1]:
                y = array[x]
                array[x] = array[x+1]
                array[x+1] = y
                d+=1
                print(" ".join(map(str, array)))
    if d==0:
        return(print(0))

N=int(input())
array=[int(i) for i in input().split()]
func(array)
