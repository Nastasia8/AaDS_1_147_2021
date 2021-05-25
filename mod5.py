#ТРЕНИРОВОЧНЫЕ ЗАДАЧИ
#задача1
class Animal:
    def __int__(self,name):
        self.__name = name

    def speak(self, voice):
        raise NotImplementedError("Класс наследник должен реализовывать новый метод")

    @property
    def name(self):
        return self.__name

class Dog(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name)
        self.__age = 1

    def speak(self, voice):
        print(self.name ," is saying", voice)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            if age >0 and age < 25:
                self.__age = age
            else:
                print("hhhhhh!")
        else:
            print("ldjdhfgdjskk")

    def show(self):
        print("name:", self.name, "age:", self.age)

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color
    def show(self):
        print("name:", self.color, "color:", self.color)

cat = Cat("Lia", "grey")
cat.speak("meow")
cat.show()
dog = Dog("Jerri")
dog.age = 12
dog.speak("gav-gav")
dog.show()

#задача2
class Node:
    __size= 0
    __height = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size+=1

    @property
    def size(self):
        return self.__size

    @property
    def height(self):
        return self.__height +1

    def add(self, value, depht):
        if self.data == value:
            return
        if value<self.data:
            if self.left:
                self.left.add(value, depht+1)
            else:
                if Node.__height < depht:
                    Node.__height = depht
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value,depht+1)
            else:
                if Node.__height < depht:
                    Node.__height = depht
                self.right = Node(value)

    def find_forcs(self):
        if self.left:
            self.left.find_forcs()
        if self.left and self.right:
            print(self.data, end =" ")
        if self.right:
            self.right.print()

    def search(self, value):
        if self.data == value:
            return True
        elif value<self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
    def print(self):
        if self.left:
            self.left.print()
        print(self.data, end =" ")
        if self.right:
            self.right.print()

def height(tree):
    if not tree:
        return 0
    return(max(height(tree.left), height(tree.right))+1)

def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i], 1)
    return root

def in_order(tree):
    if tree:
        in_otder(tree.left)
        print(tree.data, end=" ")
        in_otder(tree.right)

def pre_order(tree):
    if tree:
        print(tree.data, end=" ")
        pre_otder(tree.left)
        pre_otder(tree.right)

def post_order(tree):
    if tree:
        post_otder(tree.left)
        post_otder(tree.right)
        print(tree.data, end=" ")
def main():
    elements = [7, 3, 2, 1, 9, 5, 4, 6, 8]
    tree = build_tree(elements)
    tree.print()
    print()
    print(tree.height)
    print(height(tree))
    tree.find_forcs()
    print()
    print(tree.search(8))
    print(tree.search(7))
    print(tree.search(13))
    print(tree.search(0))

main()






#ЛЕВЫЕ ЗАДАЧИ
#задача1
class Node:
    __size = 0
    __height = 0
    def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
       Node.__size+=1
    @property
    def height(self):
       return Node.__height +1

    def add(self, data, depht):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
               self.left.add(data, depht+1)
            else:
                if Node.__height < depht:
                   Node.__height = depht
                self.left = Node(data)
        else:
            if self.right:
               self.right.add(data, depht+1)
            else:
                if Node.__height < depht:
                   Node.__height = depht
                self.right = Node(data)

    @property
    def size(self):
       return Node.__size

    def find_min(self):
        if not self.left:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.data
        return self.right.find_max()
        
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(self.data)
        return self   
        
    def print_Tree(self):
        if self.left:
           self.left.print_Tree()
        print(self.data, end=" ")
        if self.right:
           self.right.print_Tree()

    def find_forks(self):
        if self.left:
           self.left.find_forks()
        if self.left and self.right:
           print(self.data, end=" ")
        if self.right:
           self.right.find_forks()

def height(root):
    if root is None:
       return 0
    return max(height(root.left), height(root.right))+1

def build_tree(elements):
   root = Node(elements[0])
   for i in range(1, len(elements)):
       root.add(elements[i], 1)
   return root

numbers = [16,5,2,22,10,30,17,44]
tree = build_tree(numbers)
tree.print_Tree()
print()
print(tree.find_min())
print()
tree.delete(10)
tree.print_Tree()
print()
tree.delete(30)
tree.print_Tree()
print()
tree.delete(22)
tree.print_Tree()






#ПРАВЫЕ ЗАДАЧИ
задача1(максимум на отрезке)
def build(v, l, r, it, a):
    if r-l==1:
        it[v]=a[l]
        return
    m = (r+l)//2
    build(2*v+1, l,m,it,a)
    build(2*v+2, m,r,it,a)
    it[v]=max(it[v*2+1],it[v*2+2])

def get_max(v,l,r,it,ql,qr):
    if ql <= l and qr>=r:
        return it[v]
    if ql >= r or qr <= l:
        return -1e9
    m = (r+l)//2
    tl = get_max(2*v+1,l,m,it,ql,qr)
    tr = get_max(2*v+2,m,r,it,ql,qr)
    return max(tl,tr)
    
def main():
    n=int(input())
    nums = list(map(int,input().split()))
    it = [0]*4*n
    build(0, 0, n, it, nums)
    q = int(input())
    indx = []
    while q!=0:
        l, r=map(int,input().split())
        indx.append(get_max(0, 0, n, it, l-1, r))
        q-=1
    print(*indx)

main()

#задача2(индекс максимума на отрезке)
def build(v, l, r, it, a):
    if r-l==1:
        it[v]=[a[l],l]
        return
    m = (r+l)//2
    build(2*v+1, l,m,it,a)
    build(2*v+2, m,r,it,a)
    it[v]=max(it[v*2+1],it[v*2+2])

def get_max(v,l,r,it,ql,qr):
    if ql <= l and qr>=r:
        return it[v]
    if ql >= r or qr <= l:
        return [-1e9, -1]
    m = (r+l)//2
    tl = get_max(2*v+1,l,m,it,ql,qr)
    tr = get_max(2*v+2,m,r,it,ql,qr)
    return max(tl,tr)
    
def main():
    n=int(input())
    nums = list(map(int,input().split()))
    it = [[0,0]]*4*n
    build(0, 0, n, it, nums)
    q = int(input())
    indx = []
    while q!=0:
        l, r=map(int,input().split())
        indx.append(get_max(0, 0, n, it, l-1, r))
        q-=1
    for e, i in indx:
        print(i+1, end=" ")

main()

#задача3(количество максимумов на отрезке)
def build(v, l, r, it, a):
    if r-l==1:
        it[v]=[a[l],1]
        return
    m = (r+l)//2
    build(2*v+1, l,m,it,a)
    build(2*v+2, m,r,it,a)
    tl = it[2*v+1]
    tr = it[2*v+2]
    if tl[0] > tr[0]:
        it[v] = tl
    elif tl[0] < tr[0]:
        it[v] = tr
    else:
        it[v] =[tl[0],tl[1]+tr[1]]

def get_max(v,l,r,it,ql,qr):
    if ql <= l and qr>=r:
        return it[v]
    if ql >= r or qr <= l:
        return [-1e9, -1]
    m = (r+l)//2
    tl = get_max(2*v+1,l,m,it,ql,qr)
    tr = get_max(2*v+2,m,r,it,ql,qr)
    if tl[0] > tr[0]:
        return tl
    elif tl[0] < tr[0]:
        return tr
    else:
        return [tl[0],tl[1]+tr[1]]

def main():
    n=int(input())
    nums = list(map(int,input().split()))
    it = [[0,0]]*4*n
    build(0, 0, n, it, nums)
    q = int(input())
    indx = []
    while q!=0:
        l, r=map(int,input().split())
        indx.append(get_max(0, 0, n, it, l-1, r))
        q-=1
    for e, k in indx:
        print(e, k)

main()

#задача4(запрос на...)
def build(v, l, r, it, a):
    if r-l == 1: 
        it[v] = a[l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = max(it[2*v + 1], it[2*v + 2])

def get_max(v, l, r, it, ql, qr):
    if ql <= l and qr >= r: 
        return it[v]
    if ql >= r or qr <= l:
        return -1e9
    m = (l+r)//2
    tl = get_max(2*v + 1, l, m, it, ql, qr)
    tr = get_max(2*v + 2, m, r, it, ql, qr)
    return max(tl, tr)

def update(v, l, r, it, indx, val):
    if r - l == 1:
        it[v] = val
        return
    middle = (r+l)//2
    if indx < middle:
        update(v*2+1, l, middle, it, indx, val)
    else:
        update(v*2+2, middle, r, it, indx, val)
    it[v] = max(it[2*v + 1], it[2*v + 2])
    
def main():
    n = int(input())
    it = [0]*(4*n) 
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q !=0:
        type_q, l, r = map(str, input().split())
        if type_q == "s":
            res.append(get_max(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q-=1
    print(*res)
main()

#задача5
def build(v, l, r, it, a):
    if r-l == 1: 
        it[v] = [a[l], l]
        return
    m = (l+r)//2
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = max(it[2*v + 1], it[2*v + 2])

def get_max(v, l, r, it, ql, qr):
    if ql <= l and qr >= r: 
        return it[v]
    if ql >= r or qr <= l:
        return [-1e9, -1]
    m = (l+r)//2
    tl = get_max(2*v + 1, l, m, it, ql, qr)
    tr = get_max(2*v + 2, m, r, it, ql, qr)
    return max(tl, tr)

def update(v, l, r, it, indx, val):
    if r - l == 1:
        it[v][0] = val
        return
    middle = (r+l)//2
    if indx < middle:
        update(v*2+1, l, middle, it, indx, val)
    else:
        update(v*2+2, middle, r, it, indx, val)
    it[v] = max(it[2*v + 1], it[2*v + 2])
    
def main():
    n = int(input())
    it = [[0, 0]]*(4*n) 
    a = list(map(int, input().split()))[:n]
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q !=0:
        type_q, l, r = map(str, input().split())
        if type_q == "s":
            res.append(get_max(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q-=1
    for _, i in res:
        print(i+1, end=" ")
main()






#ЗАДАЧАНАКЛАССЫ
from abc import ABC, abstractmethod
from math import pi
class Figure(ABC):
    def __init__(self, color):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
       
    @color.setter
    def color(self, color):
        self.__color = color
       
    @abstractmethod
    def perimeter(self):
        pass 
    
    @abstractmethod
    def square(self):
        pass     
    
    @abstractmethod
    def info(self):
        print("color: ", self.color) 
    
class Rectangle(Figure):
    def __init__(self, color, w, h):
        super().__init__(color)
        self.__w = w
        self.__h = h

    def perimeter(self):
        return (self.__w + self.__h)*2

    def square(self):
        return self.__w * self.__h    
    
    def info(self):
        print("it\'s rectangle!")
        print("square: {0:.2f}, perimeter: {1:.2f}".format(self.square(), self.perimeter()))
        super().info()

class Circle(Figure):
    def __init__(self, color, r):
        super().__init__(color)
        self.__r = r

    def perimeter(self):
        return 2*pi*self.__r

    def square(self):
        return pi*self.__r*self.__r  
    
    def info(self):
        print("it\'s circle!")
        print("square: {0:.2f}, perimeter: {1:.2f}".format(self.square(), self.perimeter()))
        super().info()

r = Rectangle("red", 5, 4)
r.info()
g = Circle("green", 5)
g.info()
print(g.color)
g.color="Blue"
print(g.color)






#ОСНОВНЫЕ ЗАДАЧИ
#задача1
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, value):
        if self.data == value:
            return
        if value<self.data:
            if self.left:
                self.left.add(value) 
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

    def find_forcs(self):
        if self.left:
            self.left.find_forcs()
        if (self.left and not self.right) or (not self.left and self.right):
            print(self.data,)
        if self.right:
            self.right.find_forcs()

def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i],)
    return root

def main():
    elements = list(map(int, input().split()))
    elements =elements[:-1]
    tree = build_tree(elements)
    tree.find_forcs()
    
main()


#задача 2
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
    root = Node(elements[0]) #создаем элемент класса
    for i in range(1, len(elements)):
        root.add(elements[i]) #добавляем элементы в дерево
    return root

def balance(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balance(tree.right) and balance(tree.left)): #условие сущ-ния дерева, чтобы высота левого и правого отличались не больше, чем на 1, возможность выполнения метода для его правой и левой частей
        return True
    return False

numbers = [int(i) for i in input().split()] #вводим массив
numbers.pop()  #удаляем последний 0
tree = build_tree(numbers) #строим дерево
if balance(tree): #если возвращается True
    print("YES")
else:
    print("NO")


#задача 3
from math import gcd #чтобы использовать нод; ну а весь остальной код был написан с вами на занятии, только там мы  максимум искали

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
    if ql >= r or qr <= l: #если слева больше, чем справа(или наоборот), то возвращаем 0
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


#задача 5
from math import gcd 
def build(v, l, r, it, a):  #пишем какие переменные принимает функция
    if r-l == 1:        #если результат равен 1, то возвращаем
        it[v] = a[l]
        return
    m = (l+r)//2            
    build(2*v + 1, l, m, it, a)
    build(2*v + 2, m, r, it, a)
    it[v] = gcd(it[2*v + 1], it[2*v + 2])

def getNOD(v, l, r, it, ql, qr): #пишем какие переменные принимает функция
    if ql <= l and qr >= r: 
        return it[v]
    if ql >= r or qr <= l:  # если слева больше, чем справа или наоборот, то возвращаем 0
        return 0
    m = (l+r)//2
    tl = getNOD(2*v + 1, l, m, it, ql, qr) #в результате получаем НОД и строчкой ниже тоже самое
    tr = getNOD(2*v + 2, m, r, it, ql, qr)
    return gcd(tl, tr)

def update(v, l, r, it, indx, val): #пишем какие переменные принимает функция
    if r - l == 1:    #если выдает 1, то возвращаем
        it[v] = val
        return
    middle = (r+l)//2  #находим серединку
    if indx < middle:   #если индекс меньше середины, то возвращается меньшее
        update(v*2+1, l, middle, it, indx, val)
    else:
        update(v*2+2, middle, r, it, indx, val)   #если индекс большее середины, то возвращается большее
    it[v] = gcd(it[2*v + 1], it[2*v + 2])  #нашли НОД

def main():  #вот это главная функция
    n = int(input())  #это по условию и строчка ниже тоже
    it = [0]*(4*n) 
    a = list(map(int, input().split()))[:n]   #тут такие создаём списочек
    build(0, 0, n, it, a)
    q = int(input())
    res = []
    while q !=0:
        type_q, l, r = map(str, input().split())
        if type_q == "s":
            res.append(getNOD(0, 0, n, it, int(l)-1, int(r)))
        else:
            update(0, 0, n, it, int(l)-1, int(r))
        q-=1
    print(*res)  #здесь выводим результат

main()  #тут вызываем главную функцию если вы не знали))))


задачи 4 и 6 решить нереально, внатуре

могу вам смешного человечка прикрепить:

     @
   ≤((≥      хеллоу
   _| \_