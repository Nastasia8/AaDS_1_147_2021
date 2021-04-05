n = int(input())
x = 0
array = list(map(int,input().split()))

for i in range (0,n-1):
    for j in range (i+1,n):
        if array[i]>array[j] and i<j:
            x+=1
print (x)