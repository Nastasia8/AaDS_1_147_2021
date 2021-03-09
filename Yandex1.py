#Задание 1

N=int(input())

k=input().split()[:N]
arr = [int(x) for x in k]
m=0

for i in range(N-1):
    for j in range(N-1-i):
	    if arr[j+1]<arr[j]:
	        m=1
	        arr[j], arr[j+1]=arr[j+1], arr[j]
	        print(*arr, sep=" ")
if m==0:
    print(0)


#Задание 2

N=int(input())

mass=[]
for i in range(N):
    k, v=map(int, input().split())
    mass.append([k,v])
mass.sort(key=lambda x: x[0])
mass.sort(key=lambda x: x[1], reverse = True)
[print(i[0], i[1]) for i in mass]


#Задание 3

N=int(input())

p = input().split()[:N]
p = [int(x) for x in p]

def merge_sort(a):
    if len(a) == 1:
        return a
    middle = len(a) // 2
    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])
    return merge(left, right)

def merge(x,y):
    c = []
    i = j = 0
    while i < len(x) and j < len(y):
        if x[i]<y[j]:
            c.append(x[i])
            i+=1
        else:
            c.append(y[j])
            j+=1
    if i<len(x):
        c += x[i:]
        print(c.index(min(c))+1, c.index(max(c))+1, min(c), max(c))
    if j<len(y):
        c += x[j:]
        print(c.index(min(c))+1, c.index(max(c))+1, min(c), max(c))
    return c

print(*merge_sort(p), end=" ")


#Задание 5

N=int(input())
print(len(set(input().split()[:N])))


#Задание 6

N = int(input())

c = input().split()[:N]
c = [int(x) for x in c]

K = int(input())

p = input().split()[:K]
p = [int(x) for x in p]

for i in range(0,N):
    if c[i] < p.count(i + 1):
        print('yes')
    else:
        print('no')
