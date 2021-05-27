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
