from math import gcd #подключаем библиотеку для нахождения НОД

def build(v, l, r, it, nums):   #создаем функцию build
    if r-l == 1:
        it[v] = nums[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, nums)
    build(2*v+2, m, r, it, nums)
    it[v] = gcd(it[2*v+1], it[2*v+2])

def NOD(v, l, r, it, ql, qr): #создаем функцию для нахождения НОД
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = NOD(2*v+1, l, m, it, ql, qr)
    tr = NOD(2*v+2, m, r, it, ql, qr)
    return gcd(tl, tr) #возвращает НОД левого и правого значения

def main():
    n = int(input())
    num = list(map(int, input().split())) #создаем список
    it = [0]*4*n  #массив для дерева
    build(0, 0, n, it, num)
    q = int(input())
    index = []
    while q != 0:
        l, r = map(int, input().split())
        index.append(NOD(0, 0, n, it, l-1, r))
        q -= 1
    print(*index)

main()