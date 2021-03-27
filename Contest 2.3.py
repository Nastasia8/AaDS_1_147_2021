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
t = s
for i in range(len(t)):
    s_t = t+"$"+s
    p = preph(s_t)
    t = t[1:]
Sum = sum(p)
if len(s) % Sum == 0 and s[:len(s)//Sum]*Sum == s:
    print(sum(p))
else:
    print(1)
