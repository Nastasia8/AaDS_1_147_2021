class Heap():
    def __init__(self, arr):
        self.__arr = arr

    @property
    def length(self):
        return len(self.__arr)


    def print_(self):
        print(*self.__arr)


    def shift_down(self, current_indx):
        while 2*current_indx+1 < self.length:
            left_index = 2*current_indx+1
            right_index = 2*current_indx+2
            child_index = left_index
            if right_index < self.length and self.__arr[left_index] < self.__arr[right_index]:
                child_index = right_index
            if self.__arr[child_index] <= self.__arr[current_indx]:
                break
            self.__arr[current_indx], self.__arr[child_index] = self.__arr[child_index], self.__arr[current_indx]
            current_indx = child_index

    def extract(self):
        self.__arr[0], self.__arr[self.length-1] = self.__arr[self.length-1], self.__arr[0]
        value=self.__arr.pop()
        self.shift_down(0)
        return value

def build(arr):
    heap = arr[:]
    h = Heap(heap)
    for i in range(len(heap)-1, -1, -1):
        h.shift_down(i)
    return h

def main():
    n = int(input())
    a = list(map(int, input().split()))
    heap = build(a)
    res=[]
    while heap.length:        
        heap.print_()
        res.insert(0,heap.extract())
    print(*res)
main()  