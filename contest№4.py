def merge(x, y):
    res = []
    i = 0
    j = 0
    inver = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            res.append(x[i])
            i += 1
        else:
            res.append(y[j])
            j += 1
            inver += len(x) - i
    while i < len(x):
        res.append(x[i])
        i += 1
    while j < len(y):
        res.append(y[j])
        j += 1
    return res, inver

def MergeSort(L):
    n = len(L)
    if n <= 1:
        return L, 0
    middle = n//2
    x, l_inver = MergeSort(L[0:middle])    
    y, r_inver = MergeSort(L[middle:n])
    res, inver = merge(x, y)
    return res, inver + l_inver + r_inver     

N = int(input())
L = list(map(int, input().split(" ")))
L, itog_inver = MergeSort(L)
print(itog_inver)