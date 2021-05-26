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