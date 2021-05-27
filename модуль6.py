#6.1
def shift_up(index, heap): #Делали на паре
    while heap[index] > heap[(index-1)//2] and (index-1)//2 >= 0: #условие(ребенок больше родителя)
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]  #меняем местами
        index = (index-1)//2
    return index+1 #индекс больше на 1

def shift_down(index, heap):
    while 2*index+1 < len(heap): # левый индекс<размера кучи
        left_index = 2*index+1
        right_index = 2*index+2
        child_index = left_index
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            child_index = right_index
        if heap[child_index] <= heap[index]: # если 1 значение<=2 значение - выходим из цикла
            break
        heap[index], heap[child_index] = heap[child_index], heap[index] # Смена значений
        index = child_index
    return index+1 # Возвращаем индекс

def add(item, heap): #добавление элемента 
    heap.append(item)
    return shift_up(len(heap)-1, heap)

def extract(heap): #извлечение элемента
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    ind = heap.pop()
    if heap:
        return shift_down(0, heap), ind
    else:
        return 0, ind

def get_max(heap):
    return heap[0]

def main():
    heap = []  
    result = []
    input_ = input().split() #ввод данных
    n, m = int(input_[0]), int(input_[1])
    for i in range(m):
        data = input().split()
        if int(data[0]) == 1:
            if not heap: 
                result.append(-1) # если нельзя добавить элемент, тодобавляем в конец списка -1
            else: 
                result.append(extract(heap)) #вставляем в конец списка извлеченный элемент
        elif int(data[0]) == 2:
            if len(heap) == n: 
                result.append(-1)
            else:
                result.append(add(int(data[-1]), heap)) 
    for i in result:
        if type(i) == tuple:
            print(*i)
        else:
            print(i)
    print(*heap) 

main()
#6.2
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

    def add(self, value): # добавляем элемент в кучу
        if len(self.__heap) != self.__full:
            self.__heap.append(value)
            self.__result.append(self.shift_up(len(self.__heap)-1))
        else:
            self.__result.append(-1)

    def remove(self, index): 
        if index <= len(self.__heap) and index != 0: # проверка элемента на наличие в куче
            last = self.__heap[-1]
            nelast = self.__heap[index-1]
            self.__heap[index -
                        1], self.__heap[-1] = self.__heap[-1], self.__heap[index-1]
            self.__result.append(self.__heap.pop())

            if last > nelast: 
                self.shift_up(index-1)
            else:
                self.shift_down(index-1)
        else:
            self.__result.append(-1)


    def remove_max_element(self): # Удаляем max из кучи 
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
#6.3
def shift_down(v, heap): 
    while 2*v+1 < len(heap):
        left_index = 2*v+1
        right_index = 2*v+2
        index = 2*v+1
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            index = right_index
        if heap[index] <= heap[v]:
            break
        heap[v], heap[index] = heap[index], heap[v]
        v = index

def extract(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    a = heap.pop()
    shift_down(0, heap)
    return a

def get_max(heap):
    return heap[0]

def build(arr):
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def main():
    n = int(input()) #вводим n
    res = []
    numbers = list(map(int, input().split()))[:n] #вводим список
    heap = build(numbers)
    for i in range(n):
        print(*heap)
        res.append(extract(heap)) #добавляем в конец результата значение 
    res.reverse()
    print(*res) #вывод 

main()
