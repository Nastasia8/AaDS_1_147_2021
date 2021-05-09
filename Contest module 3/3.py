def fun(s):
    p = [0]*len(s)
    for i in range(len(s)-1):
        j = p[i]
        while j > 0 and s[j] != s[i+1]:
            j = p[j-1]
        if s[j] == s[i+1]:
            p[i+1] = j+1
        else:
            p[i+1] = 0
    return p

def funk(s, t, m):  
    if 1 in t:
        for i in range(len(s)):
            if t[i] == 1:
                m.append(i)
        k = s[:m[-1]]
    else:
        k = s
    [print(len(s)// len(k)) if s == k*(len(s)//len(k)) else print(1)]

S = input()
T = fun(S)

mass = []

funk(S, T, mass)