#задача 1
def prephics(s):
    p=[0]*len(s)
    for i in range (len(s)-1):
        k=p[i]
        while k>0 and s[i+1]!=s[k]:
            k=p[k-1]
        if s[i+1]==s[k]:
            p[i+1]=k+1
        else:
           p[i+1]=0
    return p

def main():
    s=input()
    t=input()
    s_t=t+"&"+s
    l=prephics(s_t)
    for i in range(len(l)):
        if l[i]==len(t):
            print(i-2*len(t),end=" ")

main()

#задача2
def get_hash(s,x,p):
    hs=0
    for i in range(len(s)):
        hs=(hs*x+ord(s[i]))%p
    return hs

def fun(s,t,x,p):
    if s!=t:
        k=1
        t=t[1:]+t[0] 
        hs=get_hash(s,x,p)
        ht=get_hash(t,x,p)
        xt=1
        for i in range(len(s)-1):
            xt=(xt*x)%p
        for i in range(len(t)-1):
            if hs==ht:
                break
            else:
                ht=(x*(ht-ord(t[i])*xt)+ord(t[i]))%p
                k+=1
        if hs==ht:
            print(k)
        else:
            print(-1)
    else:
        print(0)

def main():
    s=input() #zabcd
    t=input() #abcdz
    x=26
    p=10**9+7 #1*10^9+7
    fun(s,t,x,p)
main()

#задача3
def preph(s):
    p=[0]*len(s)
    for i in range (len(s)-1):
        k=p[i]
        while k>0 and s[i+1]!=s[k]:
            k=p[k-1]
        if s[i+1]==s[k]:
            p[i+1]=k+1
        else:
           p[i+1]=0
    return p

def main():
    s=input()
    s_t=s+"&"+s
    p=preph(s_t)
    pr=p[-1]-p[len(s)-1]
    b=len(s)//pr
    if s[:pr]*b==s:
        print(b)
    else:
        print(1)

main()

#задача4
def prefix(s):
    p = [0]*len(s)
    for i in range(len(s)-1):
        j = p[i]
        while j>0 and s[j]!=s[i+1]:
            j=p[j-1]
        if s[j]==s[i+1]:
            p[i+1]= j+1
        else:
            p[i+1]=0
    return p

def main():
    s = input()
    s_t = s+"&"+s 
    a = prefix(s_t)
    p0=a[-1]-a[len(s)-1]
    print(p0)

main()
