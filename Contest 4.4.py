
def build(v, l, r, it, a):
    if r-l == 1:
        it[v] = [a[l], l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = max(it[2*v + 1], it[2*v + 2])


def get_max(v, l, r, it, ql, qr, k):
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return -1e9
    m = (l+r)//2
    tl = get_max(2*v + 1, l, m, it, ql, qr, k)
    if k != 0 and tl[0] == 0 and ql+1 <= tl[1] and tl[1] <= qr:
        k -= 1
    elif k == 0 and tl[0] == 0:
        return tl[v]
    tr = get_max(2*v + 2, m, r, it, ql, qr, k)
    if k != 0 and tr[0] == 0 and ql+1 <= tr[1] and tr[1] <= qr:
        k -= 1
    elif k == 0:
        return [v]
    Max = max(tl[0], tr[0])
    if Max == 0 and k != 0:
        k += 1
        return Max


def update(v, l, r, it, indx, val):
    if r - l == 1:
        it[v] = val
        return
    middle = (r+l)//2
    if indx < middle:
        update(v*2+1, l, middle, it, indx, val)
    else:
        update(v*2+2, middle, r, it, indx, val)
    it[v] = max(it[2*v+1], it[2*v+2])


def main():
    n = int(input())
    it = [-1]*(4*n)
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q != 0:
        l, r, k = map(int, input().split())
        res.append(get_max(0, 0, n, it, int(l-1), int(r), int(k)))
        q -= 1
        # update(0, 0, n, it, int(l)-1, int(r))
        #q -= 1
    print(*res)


main()
