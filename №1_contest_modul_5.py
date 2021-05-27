class Node:

    __height = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @property
    def height(self):
        return self.__height + 1

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
        if not(self.left and self.right) and not(not self.left and not self.right):
            print(self.data)
        if self.right:
            self.right.find_forks()


def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i], 1)

    return root


def main():
    elements = list(map(int, input().split()))
    elements.pop(-1)
    tree = build_tree(elements)
    tree.find_forks()


main()