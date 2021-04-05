#2.3
def main():
    t = int(input())
    c = list(map(int,input().split()))[:t]
    merge(c,0,len(c))
    print(*c,sep=" ")
def merge(c,start,end):
    if end - start > 1:
        middle = (start + end) // 2
        merge(c,start,middle)
        merge(c,middle,end)
        left = c[start:middle]
        right = c[middle:end]
        internal_sort(c,left,right,start)
        print(start + 1, end, c[start], c[end-1])
def internal_sort(arr,left,right,start):
    j = i = 0
    n = start
    while i < len(right) and j < len(left):
        if left[j] > right[i]:
            arr[n] = right[i]
            i+=1
        else:
            arr[n] = left[j]
            j+=1
        n+=1
    while j < len(left):
        arr[n] = left[j]
        j+=1
        n+=1
    while i < len(right):
        arr[n] = right[i]
        i+=1
        n+=1
main()
#2.4
def merge(one, two):
    spis = []
    t = 0
    a = 0
    inversion = 0
    while t < len(one) and a < len(two):
        if one[t] <= two[a]:
            spis.append(one[t])
            t += 1
        else:
            spis.append(two[a])
            a += 1
            inversion += len(one) - t
    while t < len(one):
        spis.append(one[t])
        t += 1
    while a < len(two):
        spis.append(two[a])
        a += 1
    return spis, inversion

def merge_sort(m):
    n = len(m)
    if n <= 1:
        return m, 0
    middle = n//2
    one, left = merge_sort(m[0:middle])    
    two, right = merge_sort(m[middle:n])
    spis, inversion = merge(one, two)
    return spis, inversion + left + right    

n = int(input())
m = list(map(int, input().split(" ")))
m, fin = merge_sort(m)
print(fin)
#2.6
skl=int(input())
prod=list(map(int,input().split()))
zak=int(input())
ord=list(map(int,input().split()))
count=[0]*(skl+1)
for now in ord:
    count[now]+=1
for i in range(skl):
    if prod[i]<count[i+1]:
        print ('yes')
    else:
        print ('no')

fun()
#2.7
def func():
    long = int(input())
    let = 10
    numb = []
    array = []
    for i in range(long):
        numb.append(input())
    for number in numb:
        array.append(number)
    
    print('initial array:')
    print(', '.join(numb))
    for i in range(len(numb[0])):
        print('***')
        print('phase', i+1)
        buc = [[] for k in range(let)]
        for number in array:
            buc[int(number)//10**i % 10].append(number)
        array = []
        for j in range(let):
            array = array + buc[j]
            print('bucket', j, end=": ")
            if len(buc[j]) == 0:
                print('empty')
            else:
                print(', '.join(map(str, buc[j])))
    print('***')
    print('sorted array:')
    print(', '.join(map(str, arr)))
func()                

