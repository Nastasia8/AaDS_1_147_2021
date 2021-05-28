def shift_down(index, heap): #выбираем левого потомка, если левый и правый равны
    while 2*index+1 < len(heap):
        left_index = 2*index+1
        right_index = 2*index+2
        child_index = 2*index+1
        if right_index < len(heap) and heap[left_index] < heap[right_index]:
            child_index = right_index
        if heap[child_index] <= heap[index]:
            break
        heap[index], heap[child_index] = heap[child_index], heap[index]
        index = child_index

def extract(heap): #извлечение элемента max
    heap[0], heap[-1] = heap[-1], heap[0] #переприравнивание
    ind = heap.pop() #возвращаем элемент, удаляя из списка
    shift_down(0, heap)
    return ind

def build(arr): #строим после удаления n-1
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap

def main():
    
    result = []
    t = int(input()) #вводим длину массива
    spisok = list(map(int, input().split()))[:t] # "список"
    heap = build(spisok) #"строим"
    for i in range (t): #цикл для распаковки
        print(*heap)
        result.append(extract(heap)) #добавляем в конец извлеченный элемент в heap
    result.reverse() # по условию нужно вывести отсортированный массив
    print(*result) #вывод отсортированного массива 
 

main()