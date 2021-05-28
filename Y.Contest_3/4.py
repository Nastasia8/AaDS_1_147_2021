def preph(m,l):
    p=[0]*l
    for i in range(l-1):
        v=p[i]
        while v>0 and m[i+1]!=m[v]:
            v=p[v-1]
        if m[i+1]==m[v]:
            p[i+1]=v+1
        else:
            p[i+1]=0
    return p
str = input()
m = preph(str,len(str))
print(len(str) - m[len(m)-1])