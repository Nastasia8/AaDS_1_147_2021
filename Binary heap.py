#Задание 1
def shift_up(v, heap):
    while heap[v] > heap[(v-1)//2] and (v-1)//2 >= 0:
        heap[v], heap[(v-1) //2] = heap[(v-1)//2], heap[v]
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
        v=index
    return v+1


def main():
    n, m = map(int, input().split())
    result = []
    num = []

    for i in range(m):
        commands = list(map(int, input().split()))
        if commands[0] == 1:
            if num:
                if len(num) == 1:
                    x = num.pop()
                    result.append([0, x])
                else:
                    num[0], num[-1] = num[-1], num[0]
                    x = num.pop()
                    result.append([shift_down(0, num), x])
            else:
                result.append(-1)
        else:
            if len(num) < n:
                num.append(commands[1])
                result.append(shift_up(len(num)-1, num))
            else:
                result.append(-1)
    for item in result:
        if type(item) != int:
            print(*item)
        else:
            print(item)
    print(*num)

main()

#Задание 2
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
    val = heap[len(heap)-1]
    heap[v-1], heap[len(heap)-1] = heap[len(heap)-1], heap[v-1]
    ind = heap.pop()
    if val < ind:
        shift_down(v-1, heap)
    elif val > ind:
        shift_up(v-1, heap)
    return ind
    
def extract(heap):
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
    for i in range(m):
        data = input().split()
        if int(data[0]) == 1:
            if not heap:
                result.append(-1)
            else:
                result.append(extract(heap))
        elif int(data[0]) == 2:
            if len(heap) == n:
                result.append(-1)
            else:
                result.append(add(int(data[-1]), heap))
        elif int(data[0]) == 3:
            if len(heap) >= int(data[-1]) and int(data[-1]) > 0:
                result.append(direct_extract(int(data[-1]), heap))
            else:
                result.append(-1)

    for i in result:
        if type(i) == tuple:
            print(*i)
        else:
            print(i)
    print(*heap)

main()

#Задание 3
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
    N = int(input())
    Result = []
    Num = list(map(int, input().split()))[:N]
    heap = build(Num)
    for i in range(N):
        print(*heap)
        Result.append(extract(heap))
    Result.reverse()
    print(*Result)


main()
