def func(s):
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
s_t = s+"$"+s
h = func(s_t)
p_new = h[-1]-h[len(s)-1]
print(p_new)