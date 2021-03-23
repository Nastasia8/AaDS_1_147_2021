def zap(N):
    i = 0
    spis = [0] * N
    while i < N:
        spis[i] = list(map(int, input().split(maxsplit = 1)))
        i = i + 1
    return(spis)

def func(N, spis):
    j = 0
    while j < N - 1:
        i = 0
        while i < N - j - 1:
            if spis[i][1] != spis[i+1][1]:
                if spis[i][1] < spis[i+1][1]:
                    spis[i], spis[i+1] = spis[i+1], spis[i]
            else:
                if spis[i][0] > spis[i+1][0]:
                    spis[i], spis[i+1] = spis[i+1], spis[i]
            i = i + 1
        j = j + 1
    return(spis)

def ent(spis, N):
    i = 0
    while i < N:
        print(*spis[i])
        i = i + 1
          
N = int(input())

if 1 <= N <= 1000:
    ent(func(N, zap(N)), N)
