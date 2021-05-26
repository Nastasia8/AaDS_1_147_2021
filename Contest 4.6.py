def build(v, l, r, it, a):
    if r-l == 1:
        it[v] = a[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, a)
    build(2*v+2, m, r, it, a)
    it[v] = it[2*v+1] + it[2*v+2]


def get_zero(v, l, r, it, k):
    if k > it[v]:
        return -1
    if r - l == 1:
        return r
    m = (r+l)//2
    if it[2*v+1] >= k:
        return get_zero(2*v+1, l, m, it, k)
    else:
        return get_zero(2*v+2, m, r, it, k - it[2*v+1])


def get_sum(v, l, r, it, ql, qr):
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_sum(2*v+1, l, m, it, ql, qr)
    tr = get_sum(2*v+2, m, r, it, ql, qr)
    return tl + tr


def update(v, l, r, it, indx, val):
    if r-l == 1:
        it[v] = val
        return
    middle = (r+l)//2
    if indx < middle:
        update(2*v+1, l, middle, it, indx, val)
    else:
        update(2*v+2, middle, r, it, indx, val)
    it[v] = it[2*v+1] + it[2*v+2]

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
        request = input().split()
        
        if request[0] == "s":
            l, r, k = int(request[1]), int(request[2]), int(request[3])
            s = get_sum(0, 0, n, it, l-1, r)
            if s >= k and l > 1:
                res.append(get_zero(0, 0, n, it, k+get_sum(0, 0, n, it, 0, l-1)))
            elif s >= k and l == 1:
                res.append(get_zero(0, 0, n, it, k))
            else:
                res.append(-1)
        else:
            indx, val = int(request[1]), int(request[2])
            if val == 0:
                update(0, 0, n, it, indx-1, 1)
            else:
                update(0, 0, n, it, indx-1, 0)
        q -= 1
    print(*res)

main()
