def merge_sort(arr, start, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge_list(arr, start, mid, end)
        print(start + 1, end, arr[start], arr[end - 1])
def merge_list(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            arr[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            arr[k] = right[j]
            j = j + 1
            k = k + 1
 
n=int(input())
arr=list(map(int,input().split()))[:n]
merge_sort(arr,0,len(arr))
print(" ".join(map(str,arr))) 