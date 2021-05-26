from math import gcd
def build(v, l, r, segment_tree, nums):
    if r - l == 1:
        segment_tree[v] = nums[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, segment_tree, nums)
    build(2 * v + 2, m, r, segment_tree, nums)
    segment_tree[v] = gcd(segment_tree[2*v +1], segment_tree[2*v + 2])
 
 
def NOD(v, l, r, segment_tree, ql, qr):
    if ql <= l and qr >= r:
        return segment_tree[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    st_l = int(NOD(2*v +1, l, m, segment_tree, ql, qr))
    st_r = int(NOD(2*v + 2, m, r, segment_tree, ql, qr))
    return gcd(st_l, st_r)