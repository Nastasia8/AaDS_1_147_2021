#Задание 1
def pref(s):
    p = [0] * len(s)
    for i in range(len(s) - 1):
        k = p[i]
        while k > 0 and s[i + 1] != s[k]:
            k = p[k - 1]
        if s[i + 1] == s[k]:
            p[i + 1] = k + 1
        else:
            p[i + 1] = 0
    return p

S = input()
T = input()
a = T + "$" + S
p = pref(a)
for i in range(len(p)):
    if p[i] == len(T):
        print(i - 2 * len(T), end=" ")



#Задание 2
def hash(s, x, p):
    hash_s = 0
    for i in range(len(s)):
        hash_s = (hash_s * x + ord(s[i])) % p
    return hash_s

def rolling_hash(s, t ,x ,p):
    if s != t:
        m = 1
        t = t[1:] + t[0]
        hash_s = hash(s, x ,p)
        hash_t = hash(t, x ,p)
        x_t = 1
        for i in range(len(s) - 1):
            x_t = (x_t * x) % p
        for i in range(len(t) - 1):
            if hash_s == hash_t:
                break
            else:
                hash_t = (x * (hash_t - ord(t[i]) * x_t) + ord(t[i])) % p
                m += 1
        [print(m) if hash_s == hash_t else print(-1)]
    else:
        print(0)

def main():
    S = input()
    T = input()
    x = 26
    p = 1e9 + 7
    rolling_hash(S, T, x, p)
main()


#Задание 3
def kek(s):
    p = [0] * len(s)
    for i in range(len(s) - 1):
        j = p[i]
        while j > 0 and s[j] != s[i + 1]:
            j = p[j - 1]
        if s[j] == s[i + 1]:
            p[i + 1] = j + 1
        else:
            p[i + 1] = 0
    return p

def gg(s, t, m):  
    if 1 in t:
        for i in range(len(s)):
            if t[i] == 1:
                m.append(i)
        k = s[:m[-1]]
    else:
        k = s
    [print(len(s) // len(k)) if s == k * (len(s) // len(k)) else print(1)]

S = input()
T = kek(S)

mass = []

gg(S, T, mass)


#Задание 4
def min_len(t):
    kek = 1
    p = [0] * len(t)
    for i in range(len(t) - 1):
        j = p[i]
        while t[j] != t[i + 1] and j > 0:
            j = p[j - 1]
        if t[j] == t[i + 1]:
            p[i + 1] = j + 1
        else:
            p[i + 1] = 0
        if p[i + 1] < 2:
            kek = i + 1
    return kek 

T = input()
print(min_len(T))