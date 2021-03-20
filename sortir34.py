#задача3
def main():
    n = int(input())
    a = list(map(int,input().split()))[:n]
    merge(a,0,len(a))
    print(*a,sep=" ")

def merge(a,start,end):
    if end - start > 1:
        middle = (start + end) // 2
        merge(a,start,middle)
        merge(a,middle,end)
        left = a[start:middle]
        right = a[middle:end]
        internal_sort(a,left,right,start)
        print(start + 1, end, a[start], a[end-1])

def internal_sort(arr,left,right,start):
    j = i = 0
    k = start
    while i < len(right) and j < len(left):
        if left[j] > right[i]:
            arr[k] = right[i]
            i+=1
        else:
            arr[k] = left[j]
            j+=1
        k+=1
    while j < len(left):
        arr[k] = left[j]
        j+=1
        k+=1
    while i < len(right):
        arr[k] = right[i]
        i+=1
        k+=1
main()



#задача4
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
