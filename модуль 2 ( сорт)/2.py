m = int(input())
sps = []

def funk(sam, numb):
    for i in range(m):
        sps.append(list(map(int, input().split())))

    sps.sort(key=lambda y: y[0])
    sps.sort(key=lambda y: y[1], reverse=True)
    for i in sps:
        for x in i:
            print(x, end=' ')
        print()

funk(sps,m)