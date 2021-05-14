from math import gcd


def build(v, l, r, it, a): #задаем переменные в функции
    if r-l == 1:  # если выдает 1, то возвращаем
        it[v] = a[l]
        return
    m = (l+r)//2 # поиск m
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v+1], it[2*v+2])


def getNod(v, l, r, it, ql, qr): #задаем переменные в функции
    if ql <= l and qr >= r: # если
        return it[v]
    if ql >= r or qr <= l: # если слева больше, чем справа или наоборот, то возвращаем 0
        return 0
    m = (l+r)//2 # поиск m
    tl = getNod(2*v + 1, l, m, it, ql, qr) # в tl получаем НОД
    tr = getNod(2*v + 2, m, r, it, ql, qr) # в tr получаем НОД
    return gcd(tl, tr) # выводим НОД tl and tr


def upDate(v, l, r, it, indx, val): #задаем переменные в функции
    if r - l == 1:  # если выдает 1, то возвращаем
        it[v] = val
        return
    middle = (r+l)//2 # находим середину
    if indx < middle: # если индекс меньше середины, то возвращается меньшее
        upDate(v*2+1, l, middle, it, indx, val)
    else: # если индекс большее середины, то возвращается большее
        upDate(v*2+2, middle, r, it, indx, val)
    it[v] = gcd(it[2*v+1], it[2*v+2]) # находим НОД


def main(): #создаем функции
    n = int(input()) #ввод по условию
    it = [0]*(4*n) #ввод по условию
    a = list(map(int, input().split()))[:n] #создаеи список
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q != 0: #пока не равно нулю выполняем:
        type_q, l, r = map(str, input().split())
        if type_q == "s": # если это элементы левой или правой границы
            res.append(getNod(0, 0, n, it, int(l)-1, int(r))) #номер элемента и новое значение
        else:
            upDate(0, 0, n, it, int(l)-1, int(r))
        q -= 1
    print(*res) #выводим результат


main()