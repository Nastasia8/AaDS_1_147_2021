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
    if ((leftt-rightt) == 0 or (leftt-rightt) == 1 or (leftt-rightt) == -1) and leftt != 0 and rightt != 0:
        g(tree.left)
        g(tree.right)
    elif leftt != 0 and rightt != 0:
        global t
        t = False
        return


def main():
    elements = list(map(int, input().split()))
    elements.pop(-1)
    tree = build_tree(elements)
    if len(elements) > 2:
        global t
        t = True
        g(tree)
        if t:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")


main()
