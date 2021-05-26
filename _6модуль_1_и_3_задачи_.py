#1 задача
def shift_up(index, heap):  #этот алгоритм мы с вами вместе на паре писали
    while heap[index] > heap[(index-1)//2] and (index-1)//2 >= 0:
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
        index = (index-1)//2
    return index+1



def shift_down(index, heap):
    while 2*index+1 < len(heap):
        left_index = 2*index+1
        right_index = 2*index+2
        child_index = left_index
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            child_index = right_index
        if heap[child_index] <= heap[index]:
            break
        heap[index], heap[child_index] = heap[child_index], heap[index]
        index = child_index
    return index+1


def add(item, heap):  #добавление
    heap.append(item)
    return shift_up(len(heap)-1, heap)


def extract(heap):  #извлечение
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
    s = input().split()  
    N, Massive = int(s[0]), int(s[1])
    for i in range(Massive):  
        data = input().split()  
        if int(data[0]) == 1:  
            if not heap:
                result.append(-1) # -1, если добавить элемент нельзя - в конец
            else:  
                result.append(extract(heap)) #добавляем в конец списка извлеченный элемент
        elif int(data[0]) == 2:
            if len(heap) == N:
                result.append(-1)
            else:
                result.append(add(int(data[-1]), heap))
    for i in result:#начинаем проверять каждое значение в result
        if type(i) == tuple: #eсли тип i является кортежем, то мы выводим полученный ключ, иначе выводим само значение i
            print(*i)
        else:
            print(i)
    print(*heap) 


main()

#3 задача
def shift_down(v, heap):#снова алгоритм, который мы писали с вами
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

def extract(heap):#извлечение
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
    N = int(input()) 
    result = []
    num = list(map(int, input().split()))[:N] 
    heap = build(num)
    for i in range(N):
        print(*heap)
        result.append(extract(heap)) #здесь добавляем в конец результата значение. Я пробовала поменять на get_max() - вывод неправильный получился. Подскажите, как поменять на get_max()
    result.reverse()
    print(*result) 

main()