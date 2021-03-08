n = input()
Num = list(map(int,input().split()))
m=0

for i in range(len(Num)-1):
    for j in range(len(Num)-i-1):
        if Num[j] > Num[j+1]:
            m=1
            Num[j], Num[j+1] = Num[j+1], Num[j]
            print(*Num, sep=" ")
if m==0:
    print(0)