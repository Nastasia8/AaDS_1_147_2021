Num = input()
Num = input()
Num = Num.split()

for i in range(len(Num)):
    Num[i] = int(Num[i])

for x in range(len(Num)-1):
    for y in range(len(Num)-x-1):
        if Num[y] > Num[y+1]:
            Num[y], Num[y+1] = Num[y+1], Num[y]

for i in range(len(Num)):
    print(Num[i])
