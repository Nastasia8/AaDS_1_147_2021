def preph(m):
    p=[0]*len(m)
    for i in range(len(m)-1):
        v=p[i]
        while v>0 and m[i+1]!=m[v]:
            v=p[v-1]
        if m[i+1]==m[v]:
            p[i+1]=v+1
        else:
            p[i+1]=0
    return p
def main():
    m=input()
    t=input()
    itog=t+'&'+m
    p=preph(itog)
    for i in range(len(p)):
        if p[i]==len(t):
            print(i-2*len(t),end=' ')
          
main()