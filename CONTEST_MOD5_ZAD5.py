from math import gcd
def build(v, l, r, segment_tree, nums):
    if r - l == 1:
        segment_tree[v] = nums[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segment_tree, nums)
    build(2*v + 2, m, r, segment_tree, nums)
    segment_tree[v] = gcd(segment_tree[2*v +1], segment_tree[2*v + 2])
def update(v, l, r, segment_tree, indx, value):
    if r - l == 1:
        segment_tree[v] = value
        return
    m = (l+r)//2
    if indx < m:
        update(2*v + 1, l, m, segment_tree, indx, value)
    else:
        update(2*v + 2,m, r, segment_tree,indx, value)
    segment_tree[v] = gcd(segment_tree[2*v +1], segment_tree[2*v + 2])
 
 
def NOD(v, l, r, segment_tree, ql, qr):
    if ql <= l and qr >= r:
        return segment_tree[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    st_l = NOD(2*v +1, l, m, segment_tree, ql, qr)
    st_r = NOD(2*v + 2, m, r, segment_tree, ql, qr)
    return gcd(st_l, st_r)
 
 
def main():
    n = int(input())
    numbers = list(map(int, input().split()))[:n]
    segment_tree = [0]*4*n
    build(0, 0, n, segment_tree, numbers)
    q = int(input())
    arr = []
    while q != 0:
        type_q, l, r = map(str, input().split())
        if type_q == 's':
            arr.append(NOD(0, 0, n, segment_tree, int(l)-1, int(r)))
        else:
            update(0, 0, n, segment_tree, int(l)-1, int(r))
        q -= 1
    print(*arr)
 
 
main()
