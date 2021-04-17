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

