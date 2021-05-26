#1

s = input()
t = input()

res = t + "#" + s

def prefix(s):
    p = [0]*len(s)
    p[0] = 0
    
    for i in range(len(s)-1):
        j = p[i]
        while j > 0 and s[i+1] != s[j]:
            j = p[j-1]
        
        if s[i+1] == s[j]:
            p[i+1] = j + 1
        else:
            p[i+1] = 0
    
    return p

ress = prefix(res)

result = []

for i in range(len(ress)):
    if ress[i] == len(t):
        result.append(i - 2*len(t))
        
print(*result)

#2

def get_hash(s,x,p):
    hs=0
    for i in range (len(s)):
        hs=(hs*x+ord(s[i]))%p
    return hs

def rolling_hash(s,t,x,p):
    if s!=t:
        k=0 
        t=t[1:]+t[0]
        hs=get_hash(s,x,p)
        ht=get_hash(t,x,p)
        xt=1 
        for i in range (len(s)-1):
            xt=(xt*x)%p
        for i in range (len(t)-1):
            k+=1
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
    rolling_hash(s,t,x,p)

main()

#3

def prefix(s):
    p = [0] * len(s)
    p[0] = 0
    
    for i in range(len(s) - 1):
        j = p[i]
        while j > 0 and s[j] != s[i + 1]:
            j = p[j - 1]
        if s[j] == s[i + 1]:
            p[i + 1] = j + 1
        else:
            p[i + 1] = 0
            
    return p

def repeat(s, t, res):  
    if 1 in t:
        for i in range(len(s)):
            if t[i] == 1:
                res.append(i)
        k = s[:res[-1]]
    else:
        k = s
    [print(len(s) // len(k)) if s == k * (len(s) // len(k)) else print(1)]

S = input()
T = prefix(S)

res = []

repeat(S, T, res)

#4

def min_len(s):
    res = 1
    p = [0] * len(s)
    for i in range(len(s) - 1):
        j = p[i]
        while s[j] != s[i + 1] and j > 0:
            j = p[j - 1]
        if s[j] == s[i + 1]:
            p[i + 1] = j + 1
        else:
            p[i + 1] = 0
        if p[i + 1] < 2:
            res = i + 1
    return res 

S = input()
print(min_len(S))
