#5.2

class Node:
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
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)


def height(tree): #функция для просчета высоты
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1


def build_tree(elements): #функция для построения  
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root 


def balance_tree(tree):   # какая то функция 
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balance_tree(tree.right) and balance_tree(tree.left)):
        return True
    return False 


numbers = [int(i) for i in input().split()] #вводим  последовательность 
numbers.pop()     
tree = build_tree(numbers)
if balance_tree(tree):
    print("YES")
else:
    print("NO")


    #5.3

    from math import gcd

def build(v, l, r, it, number): #создаем функцию и переменные
    if r-l == 1:                #если результат равен 1, то возвращаем
        it[v] = number[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, number)
    build(2*v+2, m, r, it, number)
    it[v] = gcd(it[2*v+1], it[2*v+2])

def calc(v, l, r, it, ql, qr): #создаем функцию просчета наибольшего общего делителя слева и справа
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:     # если слева больше, чем справа или наоборот, то возвращаем 0
        return 0
    m = (r+l)//2
    tl = calc(2*v+1, l, m, it, ql, qr)
    tr = calc(2*v+2, m, r, it, ql, qr)
    return gcd(tl, tr)

def main():
    n = int(input()) #ввод 
    number = list(map(int, input().split())) #создание списка
    it = [0]*4*n
    build(0, 0, n, it, number)
    q = int(input())
    index = []
    while q != 0: #выполняем условие
        l, r = map(int, input().split())
        index.append(calc(0, 0, n, it, l-1, r))
        q -= 1
    print(*index)

main()


#5.5

from math import gcd

def build(v, l, r, it, a): #создаем функцию и переменные
    if r-l == 1:
        it[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v+1], it[2*v+2])    

def calc(v, l, r, it, ql, qr): #создаем функцию просчета наибольшего общего делителя на динамических подотрезках
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

def main(): #функция НОД, вводим все условия, создаем список 
    n = int(input())
    it = [0]*(4*n)
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q != 0: 
        t_q, l, r = map(str, input().split())
        if t_q == "s":
            res.append(calc(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q -= 1
    print(*res)

main()