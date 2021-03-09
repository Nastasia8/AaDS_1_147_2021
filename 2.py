d = int(input())
s=[]

for i in range(d):
    key,val =map(int,input().split())
    s.append([key,val])

for i in range(d-1):
    for q in range(d-i-1):
        if s[q][1] < s[q+1][1]:
            s[q], s[q+1] = s[q+1], s[q]
        if s[q][1] == s[q+1][1] and s[q][0] > s[q+1][0]:
            s[q], s[q+1] = s[q+1], s[q]

[print(i[0],i[1])for i in s]
