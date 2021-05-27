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


def height(tree): #функция для просчёта высоты дерева
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1


def build_tree(elements): #функция для построение дерева 
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root 


def balance_tree(tree):   #функция проверки баланса дерева по условию задачи 
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balance_tree(tree.right) and balance_tree(tree.left)):
        return True
    return False 

numbers = [int(i) for i in input().split()]
numbers.pop() #проверка дерева с конца
tree = build_tree(numbers)
if balance_tree(tree):
    print("YES")
else:
    print("NO")