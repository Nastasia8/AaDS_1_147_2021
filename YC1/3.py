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