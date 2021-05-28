from math import gcd

def build(v, l, r, it, a): #создаем ф-ю build 
    if r-l == 1:
        it[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v+1], it[2*v+2])    

def calc(v, l, r, it, ql, qr): #создаем ф-ю просчета наибольшего общего делителя на динамических подотрезках
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (l+r)//2
    tl = calc(2*v + 1, l, m, it, ql, qr)
    tr = calc(2*v + 2, m, r, it, ql, qr)
    return gcd(tl, tr) #вывод НОД для tl и tr

def update(v, l, r, it, index, value):
    if r - l == 1:
        it[v] = value
        return
    middle = (r+l)//2
    if index < middle: #если индекс меньше середины, то возвращаем большее
        update(v*2+1, l, middle, it, index, value)
    else:
        update(v*2+2, middle, r, it, index, value)
    it[v] = gcd(it[2*v+1], it[2*v+2]) #итог, получаем НОД

def main(): #ф-я НОД, создаем список 
    n = int(input())
    it = [0]*(4*n)
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q != 0: #пока q не равно 0, выполняются следующие действия
        t_q, l, r = map(str, input().split())
        if t_q == "s":
            res.append(calc(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q -= 1
    print(*res) #вывод

main()