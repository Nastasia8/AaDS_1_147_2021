def preph(s):
    p = [0]*len(s)
    for i in range(len(s)-1):
        k = p[i]
        while k > 0 and s[i+1] != s[k]:
            k = p[k-1]
        if s[i+1] == s[k]:
            p[i+1] = k+1
        else:
            p[i+1] = 0
    return p


s = input()
t = input()
s_t = t+"$"+s
p = preph(s_t)
for i in range(len(p)):
    if p[i] == len(t):
        print(i-2*len(t), end=" ")
