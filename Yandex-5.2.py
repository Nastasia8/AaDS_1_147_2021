class Node:
    def __init__(self, data):
        self.data = data # определяем метод
        self.left = None # определяем метод
        self.right = None # определяем метод

    def add(self, data):
        if data == self.data: # если равно, то возвращаем
            return
        if data < self.data: # если меньше, то добавляем в левую часть
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else: # если больше, то добавляем в правую часть
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)


def height(tree):  # функция просчета высоты
    if tree is None: # если ничего, то завершаем
        return 0
    return max(height(tree.left), height(tree.right))+1 # возвращаем макс значения


def buildTree(elements):  # функция построения дерева
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root


def balTree(tree): # проверяем балансированность дерева ( так, как описано в задании)
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balTree(tree.right) and balTree(tree.left)):
        return True # если все подоходит к этому условию, то True
    return False # иначе False


numbers = [int(i) for i in input().split()] # ввод в консоль
numbers.pop() # проверка дерева, смещаясь по -1 элементу ( i = -1)
tree = buildTree(numbers)
if balTree(tree):
    print("YES")
else:
    print("NO")
