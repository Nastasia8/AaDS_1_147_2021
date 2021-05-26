class Heap:
    def __init__(self, full):
        self.__heap = [] # Объвляем кучу
        self.__result = [] #список для результата
        self.__full = full

    
    def show_result(self): # Метод для вывода результата
        for item in self.__result:
            if type(item) == int:
                print(item)
            else:
                print(*item)
        print(*self.__heap)

    def shift_up(self, cur_index):
        while self.__heap[cur_index] > self.__heap[(cur_index-1)//2] and (cur_index-1)//2 >= 0:
            x = self.__heap[cur_index]
            self.__heap[cur_index] = self.__heap[(cur_index-1)//2]
            self.__heap[(cur_index-1)//2] = x
            cur_index = (cur_index-1)//2
        return cur_index+1

    def shift_down(self, cur_index):
        while 2*cur_index+1 < len(self.__heap):
            left_cur_index = 2*cur_index+1
            right_cur_index = 2*cur_index+2
            child_index = left_cur_index
            if right_cur_index < len(self.__heap) and self.__heap[left_cur_index] < self.__heap[right_cur_index]:
                child_index = right_cur_index
            if self.__heap[child_index] <= self.__heap[cur_index]:
                break
            self.__heap[child_index], self.__heap[cur_index] = self.__heap[cur_index], self.__heap[child_index]
            cur_index = child_index
        return cur_index+1

    def add(self, value): # Метод добавления элемента в кучу
        if len(self.__heap) != self.__full:
            self.__heap.append(value)
            self.__result.append(self.shift_up(len(self.__heap)-1))
        else:
            self.__result.append(-1)

    def remove(self, index): 
        if index <= len(self.__heap) and index != 0: # Проверяем, есть ли элемент в куче
            last = self.__heap[-1]
            nelast = self.__heap[index-1]
            self.__heap[index -
                        1], self.__heap[-1] = self.__heap[-1], self.__heap[index-1]
            self.__result.append(self.__heap.pop())
            
            if last > nelast: # Если последний изначально элемент был больше извлекаемого, то после перемещение его на место извлекаемго понимаем  иначе опускаем
                self.shift_up(index-1)
            else:
                self.shift_down(index-1)
        else:
            self.__result.append(-1)
    

    def remove_max_element(self): # Метод удаление max из кучи 
        if len(self.__heap) > 1:
            x = self.__heap[0]
            self.__heap[0], self.__heap[-1] = self.__heap[-1], self.__heap[0]
            self.__heap.pop()
            self.__result.append([self.shift_down(0), x])
        elif len(self.__heap) == 1:
            x = self.__heap.pop()
            self.__result.append([0, x])
        else:
            self.__result.append(-1)


def main():
    n, m = map(int, input().split())
    num = Heap(n)
    for i in range(m):
        commands = list(map(int, input().split()))
        if commands[0] == 1:
            num.remove_max_element()
        elif commands[0] == 2:
            num.add(commands[1])
        elif commands[0] == 3:
            num.remove(commands[1])
    num.show_result()


main()
