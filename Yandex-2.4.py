a = int(input())

def func(inversion, a):    
    count = 0
    
    for i in range(a):
        for j in range(i + 1, a):
            if array[i] > array[j]:
                count += 1
    return count



array = list(map(int, input().split()))
print(func(array, a))