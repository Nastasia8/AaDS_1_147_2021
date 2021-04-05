N = int(input())
spisok=[]

for i in range(N):
    key,val =map(int,input().split())
    spisok.append([key,val])

for i in range(N-1):
    for b in range(N-i-1):
        if spisok[b][1] < spisok[b+1][1]:
            spisok[b], spisok[b+1] = spisok[b+1], spisok[b]
        if spisok[b][1] == spisok[b+1][1] and spisok[b][0] > spisok[b+1][0]:
            spisok[b], spisok[b+1] = spisok[b+1], spisok[b]

[print(i[0],i[1])for i in spisok]
