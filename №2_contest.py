F = int(input())
y = []
for i in range(F):
    y.append(list(map(int,input().split())))
y.sort(key=lambda х: х[0])
y.sort(key=lambda х: х[1], reverse = True)
for i in y:
    for z in i:
        print(z, end = " ")
    print()
