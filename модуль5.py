#5.2
class Bub:  
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Bub(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Bub(data)

def height(tree): #просчитываем высоту дерева
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1

def build_tree(elements): #функция построения дерева
    root = Bub(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root

def balance(tree): #функция проверки баланса дерева по условию задачи 
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balance(tree.right) and balance(tree.left)):
        return True
    return False

def Ira():
    n = [int(i) for i in input().split()] #вводим последовательность (в условии) через пробел
    n.pop() #проверяем дерево с конца, перемещаясь на -1 элемент, i=-1 по умолчанию
    tree = build_tree(n)

    if balance(tree): 
        print("YES")
    else:
        print("NO")
#5.3
from math import gcd

def build(v, l, r, it, number): #создаем функцию
    if r-l == 1:
        it[v] = number[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, number)
    build(2*v+2, m, r, it, number)
    it[v] = gcd(it[2*v+1], it[2*v+2])

def Nod(v, l, r, it, ql, qr): #функция просчета НОД слева и справа
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = Nod(2*v+1, l, m, it, ql, qr)
    tr = Nod(2*v+2, m, r, it, ql, qr)
    return gcd(tl, tr)

def Ira():
    n = int(input()) #ввод данных
    number = list(map(int, input().split())) #создание списка
    it = [0]*4*n
    build(0, 0, n, it, number)
    q = int(input())
    index = []
    while q != 0: #выполняем условие, пока оно не равно 0
        l, r = map(int, input().split())
        index.append(Nod(0, 0, n, it, l-1, r))
        q -= 1
    print(*index)

Ira()
#5.5
from math import gcd

def build(v, l, r, it, a): #создаем функцию
    if r-l == 1:
        it[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v+1], it[2*v+2])    

def cac(v, l, r, it, ql, qr): #функция просчета НОД на динамических подотрезках
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (l+r)//2
    tl = cac(2*v + 1, l, m, it, ql, qr)
    tr = cac(2*v + 2, m, r, it, ql, qr)
    return gcd(tl, tr) #вывод НОД

def upd(v, l, r, it, index, value):
    if r - l == 1:
        it[v] = value
        return
    middle = (r+l)//2
    if index < middle:
        upd(v*2+1, l, middle, it, index, value)
    else:
        upd(v*2+2, middle, r, it, index, value)
    it[v] = gcd(it[2*v+1], it[2*v+2]) #получаем НОД

def ira(): 
    n = int(input()) 
    it = [0]*(4*n) # вводим необходимые условия
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = [] # создаем список
    while q != 0: #пока q не равно 0
        t_q, l, r = map(str, input().split())
        if t_q == "s":
            res.append(cac(0, 0, n, it, int(l)-1, int(r)))
        else:
            upd(0, 0, n, it, int(l)-1, int(r))
        q -= 1
    print(*res)

ira()