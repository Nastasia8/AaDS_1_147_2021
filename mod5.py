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