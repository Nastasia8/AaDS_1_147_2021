#задача3
def main():
    n=int(input())
    a=list(map(int,input().split()))[:n]
    merge(a,0,len(a))
    print(*a,sep=' ')

def merge(a,start,end):
    if end-start >1:
        middle=(start+end)//2
        merge(a,start,middle)
        merge(a,middle,end)
        left=a[start:middle]
        right=a[middle:end]
        internal_sort(a,left,right,start)
        print(start+1,end,a[start],a[end-1])
def internal_sort(arr,left,right,start):
    j=i=0 #i - right,j-left
    k=start
    while i<len(right) and j<len(left):
        if left[j]>right[i]:
            arr[k]=right[i]
            i+=1
        else:
            arr[k]=left[j]
            j+=1
        k+=1
    while j<len(left):
        arr[k]=left[j]
        j+=1
        k+=1
    while i<len(right):
        arr[k]=right[i]
        i+=1
        k+=1
main()

#задача4
def merge(fir, sec):
    res = []
    i = 0
    j = 0
    k = 0
    while i < len(fir) and j < len(sec):
        if fir[i] <= sec[j]:
            res.append(fir[i])
            i += 1
        else:
            res.append(sec[j])
            j += 1
            k += len(fir) - i
    while i < len(fir):
        res.append(fir[i])
        i += 1
    while j < len(sec):
        res.append(sec[j])
        j += 1
    return res, k

def MergeSort(L):
    n = len(L)
    if n <= 1:
        return L, 0
    middle = n//2
    A, l_inv = MergeSort(L[0:middle])    
    B, r_inv = MergeSort(L[middle:n])
    res, k = merge(fir, sec)
    return res, inv + l_inv + r_inv    

N = int(input())
L = list(map(int, input().split(" ")))
L, res_inv = MergeSort(L)
print(res_inv)

