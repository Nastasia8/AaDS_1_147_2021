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

    def print(self):
        if self.left:
            self.left.print()
        print(self.data, end=" ")
        if self.right:
            self.right.print()


def height(tree):
    if not tree:
        return 0
    return(max(height(tree.left), height(tree.right)) + 1)


def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i], 1)

    return root


def in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.data, end=" ")
        in_order(tree.right)


def pre_order(tree):
    if tree:
        print(tree.data, end=" ")
        pre_order(tree.left)
        pre_order(tree.right)


def post_order(tree):
    if tree:
        post_order(tree.left)
        post_order(tree.right)
        print(tree.data, end=" ")


def g(tree):
    leftt = height(tree.left)
    rightt = height(tree.right)
    if (leftt-rightt) == 0 or (leftt-rightt) == 1 or (leftt-rightt) == -1:
        g(tree.left)
        g(tree.right)


def main():
    elements = [7, 3, 2, 1, 9, 5, 4, 6, 8]
    tree = build_tree(elements)
    tree.print()
    print()
    print(tree.height)
    print(height(tree))

    pre_order(tree)
    g(tree)


main()
