def hsht(S, p, x):
    res = 0
    for i in range(len(S)):
        res = (res*x + ord(S[i])) % p
    return res

def func(S, T):
    p = 10**9 + 7
    x = 26
    hs = hsht(S, p, x)
    ht = hsht(T, p, x)
    xt = 1
    for i in range(len(S)-1):
        xt = (xt*x) % p
    for i in range(len(S)):
        if hs == ht:
            return i
        else:
            ht = (x * (ht - ord(T[i]) * xt) + ord(T[i])) % p
    if hs != ht:
        return('-1')
        
S = str(input())
T = str(input())
if not S == T:
    print(func(S, T))
else:
    print('0')
