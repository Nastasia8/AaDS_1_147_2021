# этот код с вами писали 
def shift_up(index, heap):   
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


def add(item, heap):  # добавление
    heap.append(item)
    return shift_up(len(heap)-1, heap)


def extract(heap):  # извлечение
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    ind = heap.pop()
    if heap:
        return shift_down(0, heap), ind
    else:
        return 0, ind


def get_max(heap):
    return heap[0]


def main():
    heap = []  # создаем пустой массив
    result = []  #создаём пустой массив
    input_ = input().split()  # ввод в консоли
    n, m = int(input_[0]), int(input_[1])
    for i in range(m):  # генерируем числа
        data = input().split()  # ввод в консоли
        if int(data[0]) == 1: 
            if not heap:                                      
                result.append(-1) # если нельзя добавить элемент,добавляем в конец списка -1
            else:  # иначе вставляем в конец списка элемент,который извлекли
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
