# писали с вами ,комментарии естть к тому,что дописать надо было
def shift_down(value, heap):
    while 2*value+1 < len(heap):
        left_ind = 2*value+1
        right_ind = 2*value+2
        ind = 2*value + 1
        if right_ind < len(heap) and heap[left_ind] < heap[right_ind]:
            ind = right_ind
        if heap[ind] <= heap[value]:
            break
        heap[value], heap[ind] = heap[ind], heap[value]
        value = ind


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
    n = int(input()) #вводим длину массива
    arr = []
    numbers = list(map(int, input().split()))[:n]
    heap = build(numbers)
    for i in range(n):
        print(*heap)
        arr.append(extract(heap)) #добавляем число в конец из экстракта
    arr.reverse()
    print(*arr) #выводим на консоль


main()
