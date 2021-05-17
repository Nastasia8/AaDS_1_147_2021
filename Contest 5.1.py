def shift_up(v, heap):
    while heap[v] > heap[(v-1)//2]:
        heap[v], heap[(v-1)//2] = heap[(v-1)//2], heap[v]
        v = (v-1)//2
    return v+1


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
    return v


def add(value, heap):
    heap.append(value)
    return shift_up(len(heap)-1, heap)


def extract(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop()
    return shift_down(0, heap)


def get_max(heap):
    return heap[0]


def build(arr):
    heap = arr[:]
    for i in range(len(heap)-1, -1, -1):
        shift_down(i, heap)
    return heap


def main():
    N, M = map(int, input().split())
    Massive = list()[:N]
    heap = build(Massive)
    while M != 0:
        q = list(map(int, input().split()))
        if q[0] == 1 and heap:
            a = get_max(heap)
            print(extract(heap)+1, a)
        elif q[0] == 2 and len(heap) < N:
            print(add(q[1], heap))
        else:
            print(-1)
        M -= 1

    print(*heap)


main()
