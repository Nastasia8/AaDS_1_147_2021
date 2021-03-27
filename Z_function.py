def z_fun(s):
    mas = [0]*len(s)
    L = R = 0
    for i in range(1, len(s)):
        if i <= R:
            mas[i] = min(mas[L-i], R-i+1)
        while mas[i]+i < len(s) and s[mas[i]] == s[mas[i]+i]:
            mas[i] += 1
        if mas[i]+i-1 > R:
            L = i
            R = mas[i]+i-1
    return mas


def main():
    s = input()
    print(z_fun(s))

main()

