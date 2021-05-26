class Heap:
    __heap = []

    @property
    def length(self):
        return len(self.__heap)

    @property
    def max(self):
        return self.__heap[0]

    def empty(self):
        return self.length == 0

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
        return value

    def extract(self):
        self.__heap[0], self.__heap[self.length -
                                    1] = self.__heap[self.length-1], self.__heap[0]
        self.__heap.pop()
        if self.__heap:
            return self.shift_down(0) + 1
        else:
            return 0

    def add(self, value):
        self.__heap.append(value)
        return self.shift_up(self.length-1)+1

    def delete(self, index):
        del_value = self.__heap[index]
        last_value = self.__heap[self.length-1]
        self.__heap[index], self.__heap[self.length -
                                        1] = self.__heap[self.length-1], self.__heap[index]
        val = self.__heap.pop()
        if del_value >= last_value:
            self.shift_down(index)
        else:
            self.shift_up(index)
        return val

    def show(self):
        print(*self.__heap)


def main():
    N, M = map(int, input().split())
    heap = Heap()
    res = []
    while M:
        q = list(map(int, input().split()))
        if q[0] == 1 and not heap.empty():
            a = str(heap.max)
            res.append(str(heap.extract()) + " " + a)
        elif q[0] == 2 and heap.length < N:
            res.append(heap.add(q[1]))
        elif q[0] == 3 and q[1] <= heap.length and q[1] > 0 and not heap.empty():
            res.append(heap.delete(q[1]-1))
        else:
            res.append(-1)
        M -= 1
    print(*res, sep="\n")
    heap.show()


main()
