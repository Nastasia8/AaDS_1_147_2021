N = int(input())
a = []
for i in range(N):
    a.append(list(map(int,input().split())))
a.sort(key=lambda х: х[0])
a.sort(key=lambda х: х[1], reverse = True)
for i in a:
    for b in i:
        print(b, end = ' ')
    print()