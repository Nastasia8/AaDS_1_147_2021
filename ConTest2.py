num = input()
Num = list(map(float,input().split()))
n = 0

for x in range(len(Num)-1):
    for y in range(len(Num)-x-1):
        if Num[y] > Num[y+1]:
            Num[y], Num[y+1] = Num[y+1], Num[y]
            n += 1

print(n)
