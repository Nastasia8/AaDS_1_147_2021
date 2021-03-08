a = int(input())
spis=[]

for i in range(a):
    key,val =map(int,input().split())
    spis.append([key,val])

for i in range(a-1):
    for j in range(a-i-1):
        if spis[j][1] < spis[j+1][1]:
            spis[j], spis[j+1] = spis[j+1], spis[j]
        if spis[j][1] == spis[j+1][1] and spis[j][0] > spis[j+1][0]:
            spis[j], spis[j+1] = spis[j+1], spis[j]
            
[print(i[0],i[1])for i in spis]
