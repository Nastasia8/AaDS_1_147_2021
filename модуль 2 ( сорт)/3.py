import operator
def main():
     n = int(input())
     m =[]
     m = list(map(int,input().split()))
     sort(m)


def sort(arr, compare=operator.lt):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr)//2
        left = sort(arr[:mid], compare)
        right = sort(arr[mid:], compare)
        print (mid,mid+1, right[0], left[-1])
        return merge(left,right, compare)
def merge(left, right, compare):
    massiv = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            massiv.append(left[i])
            i+=1
        else:
            massiv.append(right[j])
            j+=1
    while i < len(left):
        massiv.append(left[i])
        i+=1
    while j < len(right):
        massiv.append(right[j])
        j+=1
    for i in massiv:
                    
                    print(i, end=' ')
    

main()    
