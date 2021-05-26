def shift_up(index, heap):  # операция shift_up не должны поднимать элемент выше, чем это необходимо
    while heap[index] > heap[(index-1)//2] and (index-1)//2 >= 0:
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
        index = (index-1)//2
    return index+1


# в операции shift_down при равенстве левой и правой части,выбираем левую.
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


def add(item, heap):  # добавление элемента
    heap.append(item)
    return shift_up(len(heap)-1, heap)


def extract(heap):  # извлечение элемента
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
    input_ = input().split()  
    n, m = int(input_[0]), int(input_[1])
    for i in range(m):  # генерация списка чисел
        data = input().split()  
        if int(data[0]) == 1:  # если 1 элемент = 0
            if not heap:
                # добавляем в конец списка -1, если нельзя добавить элемент
                result.append(-1)
            else:  # иначе вставляем в конец списка извлеченный элемент
                result.append(extract(heap))
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