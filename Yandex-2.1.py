M = int(input())
k = input().split()[:M]
spis = [int(x) for x in k]
null = 0

for i in range(M-1):
    for j in range(M-1-i):
        if spis[j+1]<spis[j]:
            null = 1
            spis[j], spis[j+1] = spis[j+1], spis[j]
            print(*spis, sep=" ")
if null == 0:
    print(0)            