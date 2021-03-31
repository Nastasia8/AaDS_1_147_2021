def func(s):
    z = ()
    z = len(s)
    l = 0
    r = 0
    i = 1
    for i in range( i < len(s)):
        if (i <= r):
            z[i] = min(r - i + 1, z[i-l])
        while  (i+z[i] < len(s)) and (s[z[i] + i]):
            z[i] = z[i] + 1
        if (i + z[i] - 1 > r):
            l = i
            r = i + z[i] - 1
    return z    

def main():
    s = input()
    print(func(s))
  

main()       