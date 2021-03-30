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


# s = input()  # 'aaabdbaa' 'affaffaffaffaffaff''aaabdbaaaaabdbaa''abcabcabc'
# print(len(s))
# s_t = s+"$"+s*2
# p = preph(s_t)
# print(p, s_t)
# ind_start = p.index(max(p))
# p[ind_start] = -1
# ind_end = p.index(max(p))
# print(ind_end-ind_start)
s = T = input()
if s[0]*len(s) == s:
    print(1)
else:
    i = 0
    while s and len(s) > 1 and s[0] == s[-1]:
        i += 1
        s = s[1:-1]

    if s != T[0]:
        s = len(s)+i
    else:
        s = i
    t = T[:s]
    p = preph(t+'&'+T)
    p = p[len(t)+1:]
    for i in p:
        if i == 0:
            s += 1
    print(s)
