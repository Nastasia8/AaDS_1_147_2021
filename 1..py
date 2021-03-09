N = int(input())

k = input().split()[:N]
a = [int(x) for x in k]
m = 0

for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                m = 1
                a[j], a[j+1] = a[j+1], a[j]
                print(*a, sep=" ")

if m==0:
    print(0)