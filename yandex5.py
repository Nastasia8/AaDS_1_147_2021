#1

class Node:
    __size = 0
    __height = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size += 1

    @property
    def size(self):
        return self.__size

    @property
    def height(self):
        return self.__height

    def add(self, value, depth):
        if self.data == value:
            return

        if value < self.data:
            if self.left:
                self.left.add(value, depth+1)
            else:
                if Node.__height < depth:
                    Node.__height = depth
                self.left = Node(value)

        else:
            if self.right:
                self.right.add(value, depth+1)
            else:
                if Node.__height < depth:
                    Node.__height = depth
                self.right = Node(value)

    def find_forks(self):

        if self.left:
            self.left.find_forks()
            
        if self.left and not self.right:
            print(self.data)

        if self.right and not self.left:
            print(self.data)

        if self.right:
            self.right.find_forks()


def build_tree(elements):
    tree = Node(elements[0])
    for i in range(1, len(elements)-1):
        tree.add(elements[i], 1)
    return tree

def main():
    numbers = list(map(int, input().split()))
    tree = build_tree(numbers)
    tree.find_forks()
main()

#2

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


def height(tree): #высота дерева
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1 


def build_tree(elements): #построение дерева 
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root 


def balance_tree(tree):   #функция проверки баланса дерева по условию задачи 
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balance_tree(tree.right) and balance_tree(tree.left)):
        return True
    return False 


numbers = [int(i) for i in input().split()]
numbers.pop() #проверяем дерево с конца 
tree = build_tree(numbers)
if balance_tree(tree):
    print("YES")
else:
    print("NO")

#3

from math import gcd

def build(v, l, r, it, number): #строим дерево
    if r-l == 1:
        it[v] = number[l]
        return
    m = (r+l)//2
    build(2*v+1, l, m, it, number)
    build(2*v+2, m, r, it, number)
    it[v] = gcd(it[2*v+1], it[2*v+2])

def calc(v, l, r, it, ql, qr): #просчет НОД слева и справа
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (r+l)//2
    tl = calc(2*v+1, l, m, it, ql, qr)
    tr = calc(2*v+2, m, r, it, ql, qr)
    return gcd(tl, tr)

def main():
    n = int(input())
    number = list(map(int, input().split()))
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

#5

from math import gcd

def build(v, l, r, it, a): #создаем функцию build 
    if r-l == 1:
        it[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v+1], it[2*v+2])    

def calc(v, l, r, it, ql, qr): #создаем функцию просчета наибольшего общего
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
    it[v] = gcd(it[2*v+1], it[2*v+2]) #получаем НОД

def main():
    n = int(input())
    it = [0]*(4*n)
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q != 0: #пока q не равно 0, выполняется
        t_q, l, r = map(str, input().split())
        if t_q == "s":
            res.append(calc(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q -= 1
    print(*res)

main()
