def get_hash(s,x,p):
    hash=0
    for item in range(len(s)):
        hash=(hash*x+ord(s[item]))%p
    return hash
def get_new_hash (s,t,p,x):
    if s==t:
        return 0
    else:
        hs=get_hash(s,x,p)
        ht=get_hash(t,x,p)
        xt=1
        for i in range (len(s)-1):
            xt=(xt*x)%p
        for i in range(len(s)):
            if hs==ht:
                return i
                break
            else:
                ht = (x * (ht - ord(t[i]) * xt) + ord(t[i])) % p
        if hs!=ht:
            return -1
s=input()
t=input()
x=26
p=10**9+7
print(get_new_hash(s,t,p,x))