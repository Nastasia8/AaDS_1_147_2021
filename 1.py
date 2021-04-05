N = int(input())

qw = input().split()[:N]
d = [int(x) for x in qw]
m = 0

for i in range(N-1):
        for j in range(N-i-1):
            if d[j] > d[j+1]:
                m = 1
                d[j], d[j+1] = d[j+1], d[j]
                print(*d, sep=" ")

if m==0:
    print(0)