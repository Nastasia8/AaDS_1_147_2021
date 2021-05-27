def shift_up(index, heap): #на паре разбирали; поднимаем выше элемент
    while heap[index] > heap[(index-1)//2] and (index-1)//2 >= 0:
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
        index = (index-1)//2
    return index+1

def shift_down(index, heap): #выбираем левого потомка, если левый и правый равны
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

def add(item, heap): #функция добавление элемента
    heap.append(item)
    return shift_up(len(heap)-1, heap)

def extract(heap): #извлечение элемента max
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    ind = heap.pop()
    if heap:
        return shift_down(0, heap), ind
    else:
        return 0, ind

def main():
    heap = []  
    result = []
    input_ = input().split()
    n, m = int(input_[0]), int(input_[1])
    for i in range(m):
        data = input().split()
        if int(data[0]) == 1:
            if not heap:
                result.append(-1) # -1, если очередь пуста
            else:
                result.append(extract(heap)) # Вставляем в конец списка наш извлеченный элемент
        elif int(data[0]) == 2:
            if len(heap) == n:
                result.append(-1)
            else:
                result.append(add(int(data[-1]), heap))  #вставляем значение
    for i in result: #выводим результаты от запросов
        if type(i) == tuple:
            print(*i)
        else:
            print(i)
    print(*heap)  #распакова "списка" в конечном состоянии

main()