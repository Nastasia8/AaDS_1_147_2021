def min_len(t):
    kek = 1
    p = [0]*len(t)
    for i in range(len(t)-1):
        j = p[i]
        while t[j] != t[i+1] and j > 0:
            j = p[j-1]
        if t[j] == t[i+1]:
            p[i+1] = j+1
        else:
            p[i+1] = 0
        if p[i+1] < 2:
            kek = i+1
    return kek 

T = input()
print(min_len(T))