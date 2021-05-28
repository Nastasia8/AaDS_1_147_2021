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
    m_t=m+"&"+m
    r=preph(m_t)
    pr=r[-1]-r[len(m)-1] 
    p=len(m)//pr 
    if m[:pr]*p==m:  
        print(p)
    else:
        print(1)
main()