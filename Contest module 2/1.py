a=int(input())
s=input().split()[:a]
k=[int(x) for x in s]
m=0
for i in range(a-1):
    for j in range(a-1-i):
        if k[j+1]<k[j]:
            m=1
            k[j],k[j+1]=k[j+1],k[j]
            print(*k,sep=" ")
if m==0:
    print(0)