from math import gcd

def build(v, l, r, it, number): #создаем функцию build
    if r-l == 1:
        it[v] = number[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, number)
    build(2*v+2, m, r, it, number)
    it[v] = gcd(it[2*v+1], it[2*v+2])

def calc(v, l, r, it, ql, qr): #создаем функцию просчета наибольшего общего делителя слева и справа
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = calc(2*v+1, l, m, it, ql, qr)
    tr = calc(2*v+2, m, r, it, ql, qr)
    return gcd(tl, tr)

def main():
    n = int(input()) #ввод данных по условиям
    number = list(map(int, input().split())) #создание списка
    it = [0]*4*n
    build(0, 0, n, it, number)
    q = int(input())
    index = []
    while q != 0: #выполняем условие, пока оно не равно 0
        l, r = map(int, input().split())
        index.append(calc(0, 0, n, it, l-1, r))
        q -= 1
    print(*index)

main()