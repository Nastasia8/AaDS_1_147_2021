def main():
     n = int(input())
     m = list(map(int,input().split()))[:n]
     sort(m, 0, len(m))
     print(*m," ")


def sort(m, arrst, arren):
    if arren - arrst > 1:
        mid = (arrst + arren) // 2
        sort(m, arrst, mid)
        sort(m, mid, arren)
        right = m[arrst:mid]
        left = m[mid:arren]
        merge(m, left, right, arrst)
        print(arrst + 1, arren, m[arrst], m[arren-1])

    
  
def merge(arr, left, right, arrst):
    i, j = 0, 0
    t = arrst
    while i < len(right) and j < len(left):
        if left[j] > right[i]:
            arr[t] = right[i]
            i+=1
        else:
            arr[t] = left[j]
            j+=1
        t+=1      
    while j < len(left):
        arr[t] = left[j]
        j+=1
        t+=1   
    while i < len(right):
        arr[t] = right[i]
        i+=1
        t+=1   
   
    

main()    