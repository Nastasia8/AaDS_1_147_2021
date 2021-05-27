def shift_down(v, heap): #см 1 задачу
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

def extract(heap): #вынимаем самый большой элемент из кучи, передаём его назад, просеиваем
    heap[0], heap[-1] = heap[-1], heap[0]
    a = heap.pop()
    shift_down(0, heap)
    return a

def get_max(heap): #возвращаем корень
    return heap[0]

def build(arr): #строим дерево
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def main():
    n = int(input()) #вводим n
    res = []
    numbers = list(map(int, input().split()))[:n] #вводим элементы массива
    heap = build(numbers) #строим кучу
    for i in range(n): #выводим состояние кучи после удаление элемента
        print(*heap)
        res.append(extract(heap)) #добавляем в конец результата значение из extract
    res.reverse() #разворачиваем список
    print(*res) #вывод отсортированного массива

main()