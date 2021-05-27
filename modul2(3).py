def main():
    m = int(input())
    c = list(map(int,input().split()))[:m]
    merge(c,0,len(c))
    print(*c,sep=" ")
def merge(c,start,end):
    if end - start > 1:
        middle = (start + end) // 2
        merge(c,start,middle)
        merge(c,middle,end)
        left = c[start:middle]
        right = c[middle:end]
        inter_sort(c,left,right,start)
        print(start + 1, end, c[start], c[end-1])
def inter_sort(ar,left,right,start):
    j = i = 0
    k = start
    while i < len(right) and j < len(left):
        if left[j] > right[i]:
            ar[k] = right[i]
            i+=1
        else:
            ar[k] = left[j]
            j+=1
        k+=1
    while j < len(left):
        ar[k] = left[j]
        j+=1
        k+=1
    while i < len(right):
        ar[k] = right[i]
        i+=1
        k+=1
main()
