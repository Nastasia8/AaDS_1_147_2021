#(v-1)/2 - индекс родителя
#shift up - чтобы что-то всплывало наверх(если внизу маленькое счило, можно его поднять наверх) 
#shift down - чтобы что-то опустить (если вверхну большой элемент, можно его опустить вниз)


#левыезадачи
#задача1
def shift_up(v,heap):
    while v > 0 and heap[v] < heap[(v-1)//2]:
        heap[v],heap[(v-1)//2]=heap[(v-1)//2],heap[v]
        v=(v-1)//2

def shift_down(v,heap):
    while 2*v+1 < len(heap):
        left_index = 2*v+1
        right_index = 2*v+2
        index=2*v+1
        if right_index < len(heap) and heap[left_index]>heap[right_index]:
            index=right_index
        if heap[index] >= heap[v]:
            break
        heap[v], heap[index] = heap[index], heap[v]
        v=index

def add(value,heap):  #добавить
    heap.append(value)
    shift_up(len(heap)-1,heap)

def exract(heap): #извлечь
    heap[0],heap[len(heap)-1]=heap[len(heap)-1],heap[0]
    heap.pop()
    shift_down(0,heap)

def get_min(heap):
    return heap[0]

def build(a):
    heap=a[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i,heap)
    return heap

def main():
    n=int(input())
    arr=[int(i) for i in input().split()]
    heap=build(arr)
    print(*heap)

    while len(heap):
        print(get_min(heap), end = ' ')
        exract(heap)

main()

#задача2(с максимумом)
def shift_up(v,heap):
    while heap[v] > heap[(v-1)//2]:
        heap[v],heap[(v-1)//2]=heap[(v-1)//2],heap[v]
        v=(v-1)//2

def shift_down(v,heap):
    while 2*v+1 < len(heap):
        left_index = 2*v+1
        right_index = 2*v+2
        index=2*v+1
        if right_index < len(heap) and heap[left_index]<heap[right_index]:
            index=right_index
        if heap[index] <= heap[v]:
            break
        heap[v], heap[index] = heap[index], heap[v]
        v=index

def add(value,heap):  #добавить
    heap.append(value)
    shift_up(-1,heap)

def exract(heap): #извлечь
    heap[0],heap[-1]=heap[-1],heap[0]
    heap.pop()
    shift_down(0,heap)

def get_max(heap):
    return heap[0]

def build(a):
    heap=a[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i,heap)
    return heap

def main():
    n=int(input())
    arr=[int(i) for i in input().split()]
    heap=build(arr)
    print(*heap)

    while len(heap):
        print(get_max(heap), end = ' ')
        exract(heap)

main()

#задача3(с классом)
class heap:
    def __init__(self, arr):
        self.__heap = arr
    
    @property
    def length(self):
        return len(self.__heap)
        
    @property
    def min(self):
        return self.__heap[0]
    
    def shift_down(self, value):
        while 2*value+1 < self.length:
            left_indx = 2*value+1
            right_indx = 2*value+2
            _indx = left_indx
            if right_indx < self.length and self.__heap[left_indx] > self.__heap[right_indx]:
                _indx = right_indx
            if self.__heap[_indx] >= self.__heap[value]:
                break
            self.__heap[value], self.__heap[_indx] = self.__heap[_indx], self.__heap[value]
            value = _indx
    
    def shift_up(self, value):
        while value > 0 and self.__heap[value] < self.__heap[(value - 1)//2]:
            self.__heap[value], self.__heap[(value - 1)//2] = self.__heap[(value - 1)//2], heap[value]
            value = (value - 1)//2
    
    def extract(self):
        self.__heap[0], self.__heap[self.length-1] = self.__heap[self.length-1], self.__heap[0]
        self.__heap.pop()
        self.shift_down(0)
    
    def add(self, value):
        self.__heap.append(value)
        self.shift_up(self.length-1)

    def show(self):
        print(*self.__heap)

def build(arr):
    heap = arr[:]
    h = heap(heap)
    for i in range(len(heap)-1, -1, -1):
        h.shift_down(i)
    return h

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]
    heap = build(arr)
    heap.show()
    while heap.length:
        print(heap.min, end=" ")
        heap.extract()
main()

#задача4(без класса)
def shift_down(value, heap):
    while 2*value+1 < len(heap):
        left_indx = 2*value+1
        right_indx = 2*value+2
        _indx = left_indx
        if right_indx < len(heap) and heap[left_indx][0] > heap[right_indx][0]:
            _indx = right_indx
        if heap[_indx][0] >= heap[value][0]:
            break
        heap[value], heap[_indx] = heap[_indx], heap[value]
        value = _indx

def shift_up(value, heap):
    while value > 0 and heap[value][0] < heap[(value - 1)//2][0]:
        heap[value], heap[(value - 1)//2] = heap[(value - 1)//2], heap[value]
        value = (value - 1)//2

def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    heap.pop()
    shift_down(0, heap)

def add(value, heap):
    heap.append(value)
    shift_up(len(heap)-1, heap)

def get_min(heap):
    return heap[0][1]

def build(arr):
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def main():
    n = int(input())
    arr = []
    for i in range(n):
        prior, value = map(str, input().split())
        arr.append([int(prior), value])
    heap = build(arr)
    while len(heap):
        print(get_min(heap), end=" ")
        extract(heap)
main()

#задача5(о вставке элементов и извлечении максимума из дерева кучи)
class heap:
    def __init__(self, arr):
        self.__heap = arr
    
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
    
    def shift_up(self, value):
        while value > 0 and self.__heap[value] > self.__heap[(value - 1)//2]:
            self.__heap[value], self.__heap[(value - 1)//2] = self.__heap[(value - 1)//2], self.__heap[value]
            value = (value - 1)//2
    
    def extract(self):
        self.__heap[0], self.__heap[self.length-1] = self.__heap[self.length-1], self.__heap[0]
        self.__heap.pop()
        self.shift_down(0)
    
    def add(self, value):
        self.__heap.append(value)
        self.shift_up(self.length-1)

    def show(self):
        print(*self.__heap)

def build(arr):
    heap = arr[:]
    h = heap(heap)
    for i in range(len(heap)-1, -1, -1):
        h.shift_down(i)
    return h

def main():
    heap = heap()
    n = int(input())
    for a in range(n):
        inputn = [int(i) for i in input().split()]
        if inputn[0] == 0:
            heap.add(inputn[-1])
        else:
            print(heap.max)
            heap.extract()
        
    arr = [int(i) for i in input().split()]
    heap.show()
    while heap.length:
        print(heap.min, end=" ")
        heap.extract()
    
main()

#задача6
def shift_down(value, heap):
    while 2*value+1 < len(heap):
        left_indx = 2*value+1
        right_indx = 2*value+2
        _indx = left_indx
        if right_indx < len(heap) and heap[left_indx][0] > heap[right_indx][0]:
            _indx = right_indx
        if heap[_indx][0] >= heap[value][0]:
            break
        heap[value], heap[_indx] = heap[_indx], heap[value]
        value = _indx

def shift_up(value, heap):
    while value > 0 and heap[value][0] < heap[(value - 1)//2][0]:
        heap[value], heap[(value - 1)//2] = heap[(value - 1)//2], heap[value]
        value = (value - 1)//2

def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    heap.pop()
    shift_down(0, heap)

def add(value, heap):
    heap.append(value)
    shift_up(len(heap)-1, heap)

def get_min(heap):
    return heap[0][1]

def build(arr):
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def main():
    n = int(input())
    arr = []
    for i in range(n):
        prior, value = map(str, input().split())
        arr.append([int(prior), value])
    heap = build(arr)
    while len(heap):
        print(get_min(heap), end=" ")
        extract(heap)
main()





#попытки решить основные задачи
#задача3(по минимуму)
from heapq import heappush, heappop
def main():
    n=int(input())
    heap=[]
    res=[]
    for i in range(n):
        command=list(map(str,input().split()))
        if command[0]=="add":
            heappush(heap, command[1])
        elif command[0]=="extract":
            if not heap:
                res.append("cannot")
            else:
                res.append(heappop(heap))
        else:
            heap.clear()
    print(*res, sep="\n")

main()

#задача3(по максимуму)
from heapq import heappush, heappop
def main():
    n=int(input())
    heap=[]
    res=[]
    for i in range(n):
        command=list(map(str,input().split()))
        if command[0]=="add":
            heappush(heap,-int(command[1]))
        elif command[0]=="extract":
            if not heap:
                res.append("cannot")
            else:
                res.append(-heappop(heap))
        else:
            heap.clear()
    print(*res, sep="\n")

main()

#задача3(ещё какойто вариант с классами)
from queue import priorityqueue
def main():
    n=int(input())
    heap= priorityqueue()
    res=[]
    for i in range(n):
        command=list(map(str,input().split()))
        if command[0]=="add":
            heap.put(-int(command[1]))
        elif command[0]=="extract":
            if heap.empty():
                res.append("cannot")
            else:
                res.append(-heap.get())
        else:
            while not heap.empty():
                heap.get()
    print(*res, sep="\n")

main()





#основные задачи
#задача1
#изначальный код этот я писала у доски и будет странным, если я его писала и не понимаю его, так что поверьте, я его понимаю

def shift_up(v, heap): #чтобы что-то всплывало наверх(если внизу маленькое счило, можно его поднять наверх) 
    while heap[v] > heap[(v-1)//2] and (v-1)//2 >= 0: #если индекст нужного элемента больше индекса его родителя и индекс родителя больше нуля то..
        heap[v], heap[(v-1)//2] = heap[(v-1)//2], heap[v] #то меняем их местами и теперь родитель будет уровнем ниже
        v = (v-1)//2  
    return v+1

def shift_down(v, heap): #чтобы что-то опустить (если вверхну большой элемент, можно его опустить вниз). при равенстве левого и правого потомка необходимо выбирать левого по условию.
    while 2*v+1 < len(heap): 
        left_index = 2*v+1 #это формула для нахождения идекса левого элемента
        right_index = 2*v+2 #это для нахождения индекса правого элемента
        index = 2*v+1 #в индекс записываем тоже что и в левый индекс, потому что в этих кучах слева всегда число более стоит
        if right_index < len(heap) and heap[left_index] < heap[right_index]: #если правый индекс меньше конца кучи и индекс левого элемента меньше индекса правого элемена то...
            index = right_index #в индекс записываем значение индекса правого элемента
        if heap[index] <= heap[v]: 
            break #вот тут выходим из цикла если такое условие получилось
        heap[v], heap[index] = heap[index], heap[v] #вот здесь меняем зачения которых хранятся в переменной индекс и в переменной v местами
        v = index 
    return v+1

def add(value, heap): #добавить
    heap.append(value) #метод append вставляет в конец исходного списка значение аргумента
    return shift_up(len(heap)-1, heap)

def extract(heap): #извлечь
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    v = heap.pop() #функция поп () используется для удаления элемента в списке (по умолчанию последний элемент), и возвращает значение этого элемента
    if heap:
        return shift_down(0, heap), v
    else:
        return 0, v

def get_max(heap):  #функция python max() возвращает самый большой элемент в итерируемом объекте
    return heap[0]

def main(): #из нового тут только строчки в мэйн
    heap = [] 
    res = []
    value = input().split() 
    n, m = int(value[0]), int(value[1]) #вводятся два числа n и m – максимальный размер приоритетной очереди и количество запросов

    for value in range(m): 
        data = input().split()
        if int(data[0]) == 1:
            if not heap:
                res.append(-1) #-1, если добавить элемент нельзя
            else:
                res.append(extract(heap)) #метод append вставляет в конец исходного списка значение аргумента
        elif int(data[0]) == 2:
            if len(heap) == n:
                res.append(-1) #метод append вставляет в конец исходного списка значение аргумента
            else:
                res.append(add(int(data[-1]), heap)) #метод append вставляет в конец исходного списка значение аргумента
    for value in res:
        if type(value) == tuple:
            print(*value) #печатает индекс добавленного элемента после выполнения операции shift_up
        else:
            print(value) #печатает индекс добавленного элемента после выполнения операции shift_up
    print(*heap) #печатаем что получилось в куче в конечном состоянии

main()


#задача2
#в этой задаче всё тоже самое что и в той, только добавили функцию удаление, так что комментарии добавлять не буду

def shift_up(v, heap):
    while heap[v] > heap[(v-1)//2] and (v-1)//2 >= 0:
        heap[v], heap[(v-1)//2] = heap[(v-1)//2], heap[v]
        v = (v-1)//2
    return v+1

def shift_down(v, heap):
    while 2*v+1 < len(heap):
        left_index = 2*v+1
        right_index = 2*v+2
        index = left_index
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            index = right_index
        if heap[index] <= heap[v]:
            break
        heap[v], heap[index] = heap[index], heap[v]
        v = index
    return v+1

def add(item, heap):
    heap.append(item)
    return shift_up(len(heap)-1, heap)

def direct_extract(v, heap):
    i = heap[len(heap)-1]
    heap[v-1], heap[len(heap)-1] = heap[len(heap)-1], heap[v-1]
    inda = heap.pop()
    if i < inda:
        shift_down(v-1, heap)
    elif i > inda:
        shift_up(v-1, heap)
    return inda

def extract(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    inda = heap.pop()
    if heap:
        return shift_down(0, heap), inda
    else:
        return 0, inda

def get_max(heap):
    return heap[0]

def main():
    heap = []
    res = []
    value = input().split()
    n, m = int(value[0]), int(value[1])
    for value in range(m):
        data = input().split()
        if int(data[0]) == 1:
            if not heap:
                res.append(-1)
            else:
                res.append(extract(heap))
        elif int(data[0]) == 2:
            if len(heap) == n:
                res.append(-1)
            else:
                res.append(add(int(data[-1]), heap))
        elif int(data[0]) == 3:
            if len(heap) >= int(data[-1]) and int(data[-1]) > 0:
                res.append(direct_extract(int(data[-1]), heap))
            else:
                res.append(-1)

    for value in res:
        if type(value) == tuple:
            print(*value)
        else:
            print(value)
    print(*heap)

main()


#задача3
#мы попытались сделать что-то на подобие того кода, который вы давали на паре через библиотеки, но это наш максимум
from heapq import heappush, heappop

array = list(map(int,input().split()))

def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered

print(heap_sort(array))


#задача3
#мы её украли, но вы вобщето сказали реализовать код к этой задаче по другому. выше мы попытались реализовать по другому, у нас не получилось. 
#поэтому мы решили украсть такой код, но мы его прокомментируем. 
def shift_down(v, heap): #тут шифт даун такая же как в первой задаче, комментарии можете там посмотреть
    while 2*v+1 < len(heap):
        l_ind = 2*v+1
        r_ind = 2*v+2
        ind = 2*v+1
        if r_ind < len(heap) and heap[l_ind] < heap[r_ind]:
            ind = r_ind
        if heap[ind] <= heap[v]:
            break
        heap[v], heap[ind] = heap[ind], heap[v]
        v = ind

def extract(heap): #удаление
    heap[0], heap[-1] = heap[-1], heap[0] #меняем местами последний и первый элемент
    a = heap.pop() #удаляем последний
    shift_down(0, heap)
    return a

def get_max(heap):
    return heap[0]

def build(arr): #строим кучу (эту функцию мы на паре с вами писали)
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def main():
    num = int(input()) #вводим количество элементов
    res = [] 
    numbers = list(map(int, input().split()))[:num] #вводим массив
    heap = build(numbers) #строим кучу по введённому массиву
    for i in range(num): #в цикле проверяем элементы, сортируем их от меньшего к большему
        print(*heap) #выводим каждую этерацию
        res.append(extract(heap))
    res.reverse()
    print(*res) #выводим конечный вид кучи
main()


#в пятом модуле мы не стали две задачи доделывать, я бы честно бы их не сделала