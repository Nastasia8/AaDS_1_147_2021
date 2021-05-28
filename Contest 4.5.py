from math import gcd


def build(v, l, r, it, a):
    if r-l == 1:
        it[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v+1], it[2*v+2])


def get_NOD(v, l, r, it, ql, qr):
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (l+r)//2
    tl = get_NOD(2*v + 1, l, m, it, ql, qr)
    tr = get_NOD(2*v + 2, m, r, it, ql, qr)
    return gcd(tl, tr)


def update(v, l, r, it, indx, val):
    if r - l == 1:
        it[v] = val
        return
    middle = (r+l)//2
    if indx < middle:
        update(v*2+1, l, middle, it, indx, val)
    else:
        update(v*2+2, middle, r, it, indx, val)
    it[v] = gcd(it[2*v+1], it[2*v+2])


def main():
    n = int(input())
    it = [0]*(4*n)
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q != 0:
        type_q, l, r = map(str, input().split())
        if type_q == "s":
            res.append(get_NOD(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q -= 1
    print(*res)


main()
