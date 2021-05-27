#6.1
def shift_up(index, heap): #на паре
    while heap[index] > heap[(index-1)//2] and (index-1)//2 >= 0: #условие
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]  #меняем местами
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
                result.append(-1) #добавляем в конец списка -1, если нельзя добавить элемент
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

def shift_up(c, heap_):
    while heap_[c] > heap_[(c-1)//2] and (c-1)//2 >= 0:
        heap_[c], heap_[(c-1)//2] = heap_[(c-1)//2], heap_[c]
        c = (c-1)//2
    return c+1

def shift_down(c, heap_):
    while 2*c+1 < len(heap_):
        left = 2*c+1
        right = 2*c+2
        child = left
        if  right < len(heap_) and heap_[left] < heap_[right]:
            child = right
        if heap_[child] <= heap_[c]:
            break
        heap_[c], heap_[child] = heap_[child], heap_[c]
        c = child
    return c+1

def add(item, heap_):  #добавление элемента
    heap_.append(item)
    return shift_up(len(heap_)-1, heap_)

def extract(heap_):   #извлечение элемента
    if len(heap)==1:
        x = heap_.pop()
        return [0, x]
    else:
        heap_[0], heap_[len(heap_)-1] = heap_[len(heap_)-1], heap_[0]
        x = heap_.pop()
        y = shift_down(0, heap_)
        return [y, x]

def extract_2_o(item, heap_):  
    v = heap[len(heap)-1]
    heap_[item], heap_[len(heap_)-1] = heap_[len(heap_)-1], heap_[item]  #меняем местами
    index_ = heap.pop()
    if v > index_:
        shift_up(item, heap_)
    else:
        shift_down(item, heap_)
    return index_


n = list(map(int,input().split()))
final_heap = []
heap = []
for i in range(n[1]):
    op = list(map(int, input().split()))
    if op[0] == 1:
        if heap:
            final_heap.append(extract(heap))
        else:
            final_heap.append(-1)
    elif op[0] == 2:
        if len(heap) < n[0]:
            final_heap.append(add(op[1], heap))
        else:
            final_heap.append(-1)
    else:
        if len(heap) >= op[1] and op[1] > 0:
            final_heap.append(extract_2_o(op[1]-1, heap))
        else:
            final_heap.append(-1)

for i in final_heap:
    if type(i) == list:
        print(*i)
    else:
        print(i)
print(*heap)




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