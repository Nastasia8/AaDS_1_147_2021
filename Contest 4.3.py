def build(v, l, r, it, nums):
    if r-l <= 2:
        it[v] = NOD(nums[l], nums[r-1])
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, nums)
    build(2*v+2, m, r, it, nums)
    it[v] = NOD(it[2*v+1], it[2*v+2])


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def get_NOD(v, l, r, it, ql, qr):
    if qr-ql <= 2:
        return it[v]
    if ql >= r or qr <= 1:
        return 1
    m = (r+l)//2
    tl = get_NOD(2*v+1, l, m, it, ql, qr)
    tr = get_NOD(2*v+2, m, r, it, ql, qr)
    return NOD(tl, tr)


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    it = [0]*4*n
    build(0, 0, n, it, nums)
    q = int(input())
    index = []
    while q != 0:
        l, r = map(int, input().split())
        index.append(get_NOD(0, 0, n, it, l-1, r))
        q -= 1
    print(*index)


main()
