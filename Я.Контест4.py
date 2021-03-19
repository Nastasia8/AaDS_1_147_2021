def merge(A, B):
    res = []
    i = 0
    j = 0
    inver = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
            inver += len(A) - i
    while i < len(A):
        res.append(A[i])
        i += 1
    while j < len(B):
        res.append(B[j])
        j += 1
    return res, inver

def MergeSort(L):
    n = len(L)
    if n <= 1:
        return L, 0
    middle = n//2
    A, l_inver = MergeSort(L[0:middle])    
    B, r_inver = MergeSort(L[middle:n])
    res, inver = merge(A, B)
    return res, inver + l_inver + r_inver     

N = int(input())
L = list(map(int, input().split(" ")))
L, itog_inver = MergeSort(L)
print(itog_inver)
