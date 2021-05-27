#2.1
I = int(input())

k = input().split()[:I]
a = [int(x) for x in k]
m = 0

for i in range(I-1):
        for j in range(I-i-1):
            if a[j] > a[j+1]:
                m = 1
                a[j], a[j+1] = a[j+1], a[j]
                print(*a, sep=" ")

if m==0:
    print(0)
#2.2
N = int(input())
spisok=[]

for i in range(N):
    key,val =map(int,input().split())
    spisok.append([key,val])

for i in range(N-1):
    for b in range(N-i-1):
        if spisok[b][1] < spisok[b+1][1]:
            spisok[b], spisok[b+1] = spisok[b+1], spisok[b]
        if spisok[b][1] == spisok[b+1][1] and spisok[b][0] > spisok[b+1][0]:
            spisok[b], spisok[b+1] = spisok[b+1], spisok[b]

[print(i[0],i[1])for i in spisok]
#2.3
def merge_sort(I,start, end):
    if len(I)>1:
        mid=len(I)//2
        left=I[:mid]
        right=I[mid:]
      

        merge_sort(left, start, start+mid-1)
        merge_sort(right, start+mid, end)
    
        i, j, k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                I[k]=left[i]
                i+=1
            else:
                I[k]= right[j]
                j+=1
            k+=1

        while j <len(right):
            I[k]=right[j]
            j+=1
            k+=1
        while i <len(left):
            I[k]=left[i]
            i+=1
            k+=1
        print(start, end, I[0], I[-1])
    return I

n = int(input())
I= list(map(int, input().split()))[:n]
merge_sort(I,1,len(I))
print(*I)
#2.4
def merge_sort(I, ir):

    if len(I) > 1:
        mid = len(I)//2
        left = I[:mid]
        right = I[mid:]
        
        ir = merge_sort(left, ir)
        ir = merge_sort(right, ir)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                I[k] = left[i]
                i += 1
            else:
                I[k] = right[j]
                j = j+1
                ir += len(left)-i
            k = k+1
        while i < len(left):
            I[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            I[k] = right[j]
            j = j+1
            k = k+1

    return ir


ir = 0
n = int(input())
I = list(map(int, input().split()))[:n]
ir = merge_sort(I, ir)
print(ir)
#2.5
am={}
d=int(input())
l=input()
n=l.split()
for i in n:
    am[i]=1
print(len(am))
#2.6
skl1= int(input())
am = list(int(i) for i in input().split(" "))[:skl1]
skl2 = int(input())
q = list(int(i) for i in input().split(" "))[:skl2]

for i in range(0, skl2):
    am[q[i]-1] -= 1

for i in range(0, skl1):
    if (am[i] < 0):
        print("yes")
    else:
        print("no")
#2.7
Array = []
length = int(input())
 
for i in range(length):
    Array.append(input())
 
print("Initial array:")
 
print(', '.join(Array))
 
 
Count = len(Array[0])
Phase=0
rang=10
for i in range(Count-1,-1,-1):
    Phase+=1
    print('**********')
    print(f'Phase {Phase}')
    bucket = [[] for _ in range(rang)]
    for j in range(len(Array)):
        bucket[ord(Array[j][i]) - ord('0')].append(Array[j])
    for j in range(rang):
        if len(bucket[j])==0:
            print(f'Bucket {j}: empty')
        else:
            print("Bucket "+str(j)+": ", end='')
            for now in range(len(bucket[j])-1):
                print(bucket[j][now],end=', ')
            print(bucket[j][len(bucket[j])-1])
    p = 0
    for j in range(rang):
        for k in range(len(bucket[j])):
            Array[p] = bucket[j][k]
            p += 1
 
print('**********')
print("Sorted array:")
 
print(', '.join(Array))       

