class Heap:

    __heap = []

    @property
    def length(self):
        return len(self.__heap)

    @property
    def max(self):
        return self.__heap[0]

    def shift_down(self, value):
        while 2*value+1 < self.length:
            left_indx = 2*value+1
            right_indx = 2*value+2
            _indx = left_indx
            if right_indx < self.length and self.__heap[left_indx] < self.__heap[right_indx]:
                _indx = right_indx
            if self.__heap[_indx] <= self.__heap[value]:
                break
            self.__heap[value], self.__heap[_indx] = self.__heap[_indx], self.__heap[value]
            value = _indx
        return value

    def shift_up(self, value):
        while value > 0 and self.__heap[value] > self.__heap[(value - 1)//2]:
            self.__heap[value], self.__heap[(
                value - 1)//2] = self.__heap[(value - 1)//2], self.__heap[value]
            value = (value - 1)//2
        return value+1

    def extract(self):
        self.__heap[0], self.__heap[self.length -
                                    1] = self.__heap[self.length-1], self.__heap[0]
        self.__heap.pop()
        v = self.shift_down(0)
        if self.__heap:
            return v+1
        else:
            return 0

    def delete(self, index):
        print(self.__heap[index])
        self.__heap[index], self.__heap[self.length -
                                        1] = self.__heap[self.length-1], self.__heap[index]
        self.extract()

    def add(self, value):
        self.__heap.append(value)
        return self.shift_up(self.length-1)

    def show(self):
        print(*self.__heap)


def build(arr):
    heap = arr[:]
    he = Heap(heap)
    for i in range(len(heap)-1, -1, -1):
        he.shift_down(i)
    return he


def main():
    N, M = map(int, input().split())
    heap = Heap()
    while M != 0:
        q = list(map(int, input().split()))
        if q[0] == 1 and heap.length != 0:
            a = heap.max
            print(heap.extract(), a)
        elif q[0] == 2 and heap.length < N:
            print(heap.add(q[1]))
        elif q[0] == 3 and q[1] <= heap.length and q[1] > 0:
            heap.delete(q[1]-1)
        else:
            print(-1)
        M -= 1

    heap.show()


main()
