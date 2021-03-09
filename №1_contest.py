def bubble(array):
    swap = 0
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
                swap +=10
                print(' '.join(map(str, array)))
    if swap == 0:
        return(print(0))
N = int(input())
array = [int(i) for i in input().split()]
bubble(array)
