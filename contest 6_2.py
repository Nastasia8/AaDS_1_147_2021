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
    if i < inda: #просеиваем в зависимости от положения удалённого элемента
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
            if len(heap) >= int(data[-1]) and int(data[-1]) > 0: #нужно удалить элемент
                res.append(direct_extract(int(data[-1]), heap)) #получаем значение удалённого элемента
            else:
                res.append(-1) #нечего удалять
    for value in res:
        if type(value) == tuple:
            print(*value)
        else:
            print(value)
    print(*heap)

main()