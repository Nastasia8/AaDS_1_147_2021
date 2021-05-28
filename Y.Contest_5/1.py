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

    def find_branches(self):
        if self.left:
            self.left.find_branches()
        if self.left and not self.right:
            print(self.data)
        if not self.left and self.right:
            print(self.data)
        if self.right:
            self.right.find_branches()

def height(root):
    if root is None:
       return 0
    return max(height(root.left), height(root.right))+1



def build_tree(elements):
   root = Node(elements[0])
   for i in range(1, len(elements)):
       root.add(elements[i], 1)
   return root


elements = list(map(int,input().split()))
elements.pop()
tree = build_tree(elements)
tree.find_branches()