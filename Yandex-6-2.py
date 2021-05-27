
def shiftUp(ind, heap):
    while heap[ind] > heap[(ind-1)//2] and (ind-1)//2 >= 0:
        heap[ind], heap[(ind-1)//2] = heap[(ind-1)//2], heap[ind]
        ind = (ind-1)//2
    return ind+1


def shiftDown(ind, heap):
    while 2*ind+1 < len(heap):
        left = 2*ind+1
        right = 2*ind+2
        child = left
        if right < len(heap) and heap[left] < heap[right]:
            child = right
        if heap[child] <= heap[ind]:
            break
        heap[ind], heap[child] = heap[child], heap[ind]
        ind = child
    return ind+1


def add(item, heap):
    heap.append(item)
    return shiftUp(len(heap)-1, heap)


def extract(heap):
    if len(heap) == 1:
        x = heap.pop()
        return [0, x]
    else:
        heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
        x = heap.pop()
        y = shiftDown(0, heap)
        return [y, x]


def extract_2_o(item, heap):
    v = heap[len(heap)-1]
    heap[item], heap[len(heap)-1] = heap[len(heap)-1], heap[item]
    index = heap.pop()
    if v > index:
        shiftUp(item, heap)
    else:
        shiftDown(item, heap)
    return index


n = list(map(int, input().split()))
finalHeap = []
heap = []
for i in range(n[1]):
    op = list(map(int, input().split()))
    if op[0] == 1:
        if heap:
            finalHeap.append(extract(heap))
        else:
            finalHeap.append(-1)
    elif op[0] == 2:
        if len(heap) < n[0]:
            finalHeap.append(add(op[1], heap))
        else:
            finalHeap.append(-1)
    else:
        if len(heap) >= op[1] and op[1] > 0:
            finalHeap.append(extract_2_o(op[1]-1, heap))
        else:
            finalHeap.append(-1)

for i in finalHeap:
    if type(i) == list:
        print(*i)
    else:
        print(i)
print(*heap)
