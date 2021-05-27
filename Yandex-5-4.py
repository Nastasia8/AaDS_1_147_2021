def build(v, l, r, it, a):
    if r-l == 1:
        it[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, a)
    build(2*v+2, m, r, it, a)
    it[v] = it[2*v+1] + it[2*v+2]


def getZero(v, l, r, it, k):
    if k > it[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if it[2*v+1] >= k:
        return getZero(2*v+1, l, m, it, k)
    else:
        return getZero(2*v+2, m, r, it, k - it[2*v+1])


def getSum(v, l, r, it, ql, qr):
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = getSum(2*v+1, l, m, it, ql, qr)
    tr = getSum(2*v+2, m, r, it, ql, qr)
    return tl + tr


def main():
    n = int(input())
    a = []
    for i in input().split():
        if int(i) == 0:
            a.append(1)
        else:
            a.append(0)
    it = [0]*4*n
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q != 0:
        l, r, k = map(int, input().split())
        s = getSum(0, 0, n, it, l-1, r)
        if s >= k and l > 1:
            res.append(getZero(0, 0, n, it, k+getSum(0, 0, n, it, 0, l-1)))
        elif s >= k and l == 1:
            res.append(getZero(0, 0, n, it, k))
        else:
            res.append(-1)
        q -= 1
    print(*res)


main()
