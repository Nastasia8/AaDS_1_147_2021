a = int(input())
b = list(map(int,input().split()))[:n]
c = int(input())
d = list(map(int,input().split()))[:c]

for i in range(n):
    if b[i] < d.count(i+1):
        print("yes")
    else:
        print("no")