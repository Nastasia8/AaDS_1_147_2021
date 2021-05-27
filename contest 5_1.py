class treeNode: #класс вершины
    __size = 0 #кол-во вершин
    def __init__(self, data): #конструктор для объектов класса
        self.data = data
        self.left = None
        self.right = None
        treeNode.__size += 1

    def add(self, value): #добавляем новую вершину
        if value == self.data:
            return
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = treeNode(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = treeNode(value)

    def findFork(self): #ищем вершину с одним ребёнка
        if self.left: #может дочерняя вершина слева - ветка? продолжаем поиск
            self.left.findFork()
        if (self.left and self.right is None) or (self.left is None and self.right): #может эта вершина и есть ветка?
            print(self.data) #да? отлично! печатаем.
        if self.right: #может дочерняя вершина справа - ветка? продолжаем поиск
            self.right.findFork()

def buildTree(elements): #строим дерево
    result = treeNode(elements[0])
    for i in range(1, len(elements)):
        result.add(elements[i])
    return result

def main():
    numbers = list(map(int, input().split(" "))) #получаем все вершины
    numbers.pop() #избавляемся от нуля
    tree = buildTree(numbers) #строим дерево
    tree.findFork() #выводим все ветки
 
main()