def get_hash(s,x,p):
    hs=0
    for i in range (len(s)):
        hs=(hs*x+ord(s[i]))%p
    return hs
def fun (s,t,x,p):
    if s!=t:
        k=1 
        t=t[1:]+t[0]#bcdza
        hs=get_hash(s,x,p)
        ht=get_hash(t,x,p)
        xt=1 
        for i in range (len(s)-1):
            xt=(xt*x)%p
        for i in range (len(t)-1):
            if hs==ht:
                break
            else:
                ht=(x*(ht-ord(t[i])*xt)+ord(t[i]))%p
        if hs==ht:
            print(k)
        else:
            print(-1)
    else:
        print(0)
    
def main():
    s=input()
    t=input()
    x=26
    p=1e9+7
    fun(s,t,x,p)

main()    