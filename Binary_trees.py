#Задание 1
class Node:
    __size = 0
    __height = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size+=1

    def add(self, value, depht):
        if self.data == value:
            return
        if value < self.data:
            if self.left:
                self.left.add(value, depht+1)
            else:
                if Node.__height < depht:
                    Node.__height = depht
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value, depht+1)
            else:
                if Node.__height < depht:
                    Node.__height = depht
                self.right = Node(value)

    def find_forks(self):
        if self.left:
            self.left.find_forks()
        if self.left or self.right:
            if self.left and not self.right:
                print(self.data, end =" ")
            elif not self.left and self.right:
                print(self.data, end =" ")
        if self.right:
            self.right.find_forks()

def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i], 1)

    return root

def main():
    p = list(map(int, input().split(" ")))
    elements = p[:-1]
    tree = build_tree(elements)
    tree.find_forks()

main()


#Задание 2
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


def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1


def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root


def balance(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balance(tree.right) and balance(tree.left)):
        return True
    return False


numbers = [int(i) for i in input().split()]
numbers.pop()
tree = build_tree(numbers)
if balance(tree):
    print("YES")
else:
    print("NO")


#Задание 3
from math import gcd

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
    it = [0]*4*n
    build(0, 0, n, it, nums)
    q = int(input())
    index = []
    while q != 0:
        l, r = map(int, input().split())
        index.append(get_NOD(0, 0, n, it, l-1, r))
        q -= 1
    print(*index)

main()


#Задание 5
from math import gcd   #основной вопрос, почему с импортированной функцией быстрее?

def build(v, l, r, it, a):
    if r-l == 1:
        it[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v+1], it[2*v+2])    


def NOD(v, l, r, it, ql, qr):
    if ql <= l and qr >= r:
        return it[v]
    if ql >= r or qr <= l:
        return 0
    m = (l+r)//2
    tl = NOD(2*v + 1, l, m, it, ql, qr)
    tr = NOD(2*v + 2, m, r, it, ql, qr)
    return gcd(tl, tr)


def update(v, l, r, it, indx, val):
    if r - l == 1:
        it[v] = val
        return
    middle = (r+l)//2
    if indx < middle:
        update(v*2+1, l, middle, it, indx, val)
    else:
        update(v*2+2, middle, r, it, indx, val)
    it[v] = gcd(it[2*v+1], it[2*v+2])


def main():
    n = int(input())
    it = [0]*(4*n)
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q != 0:
        type_q, l, r = map(str, input().split())
        if type_q == "s":
            res.append(NOD(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q -= 1
    print(*res)

main()
