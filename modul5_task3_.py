from math import gcd #подключаем библиотеку для нахождения НОД

def build(v, l, r, it, nums):  
    if r-l == 1:
        it[v] = nums[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, nums)
    build(2*v+2, m, r, it, nums)
    it[v] = gcd(it[2*v+1], it[2*v+2])

def get_NOD(v, l, r, it, ql, qr):
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = get_NOD(2*v+1, l, m, it, ql, qr)
    tr = get_NOD(2*v+2, m, r, it, ql, qr)
    return gcd(tl, tr)

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    it = [0]*4*n  #массив для дерева
    build(0, 0, n, it, nums)
    q = int(input())
    index = []
    while q != 0:
        l, r = map(int, input().split())
        index.append(get_NOD(0, 0, n, it, l-1, r))
        q -= 1
    print(*index)

main()


