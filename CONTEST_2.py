N = int(input())
how = []
for i in range(N):
    how.append(list(map(int,input().split())))
how.sort(key=lambda х: х[0])
how.sort(key=lambda х: х[1], reverse = True)
for i in how:
    for b in i:
        print(b, end = ' ')
    print()