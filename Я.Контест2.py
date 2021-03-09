v = int(input())
nab = []
for i in range(v):
    nab.append(input())
    nab[i] = nab[i].split(" ")
    for j in range(len(nab[i])):
        nab[i][j] = int(nab[i][j])

for i in range(v-1):
    for j in range(v - i - 1):
        if nab[j][1] < nab[j+1][1]:
            nab[j], nab[j+1] = nab[j+1], nab[j]
for i in range(v-1):
    for j in range(v - i - 1):
            if nab[j][1] == nab[j+1][1]:
                if nab[j][0] > nab[j+1][0]:
                    nab[j], nab[j+1] = nab[j+1], nab[j]
for i in range(v):
    stroka = ""
    stroka += str(nab[i][0])
    for j in range(1,len(nab[i])):
        stroka+=" "
        stroka+=str(nab[i][j])
    print(stroka)
