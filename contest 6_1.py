def shift_up(v, heap): #просеиваем вверх переданный элемент
    while heap[v] > heap[(v-1)//2] and (v-1)//2 >= 0: #если индекст нужного элемента больше индекса его родителя и индекс родителя больше нуля то..
        heap[v], heap[(v-1)//2] = heap[(v-1)//2], heap[v] #то меняем их местами и теперь родитель будет уровнем ниже
        v = (v-1)//2  
    return v+1

def shift_down(v, heap): #просеиваем вниз переданный элемент
    while 2*v+1 < len(heap): 
        left_index = 2*v+1 #идекса левого элемента
        right_index = 2*v+2 #индекса правого элемента
        index = 2*v+1 #левое направление более приоритетное
        if right_index < len(heap) and heap[left_index] < heap[right_index]: #ставим правый индекс если всё-таки левый меньше
            index = right_index 
        if heap[index] <= heap[v]: 
            break #всё уже как надо, ливаем
        heap[v], heap[index] = heap[index], heap[v] #опускаем элемент вниз
        v = index 
    return v+1

def add(value, heap): #добавляем вершину
    heap.append(value) 
    return shift_up(len(heap)-1, heap)

def extract(heap): #вынимаем самый большой элемент из кучи, передаём его назад, просеиваем
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    v = heap.pop() 
    if heap:
        return shift_down(0, heap), v
    else:
        return 0, v

def main(): 
    heap = [] 
    res = []
    value = input().split() 
    n, m = int(value[0]), int(value[1]) #вводим максимальный размер приоритетной очереди и количество запросов
    for value in range(m): #вводим запрос и сразу обрабатываем
        data = input().split()
        if int(data[0]) == 1: #нужен максимальный элемент
            if not heap:
                res.append(-1) #очередь пуста
            else:
                res.append(extract(heap)) #запрашиваем максимальный элемент
        elif int(data[0]) == 2: #нужно добавить элемент
            if len(heap) == n:
                res.append(-1) #куча заполнена
            else:
                res.append(add(int(data[-1]), heap)) #не заполнена? ладно, добавляем
    for i in res: #выводим результаты запросоув
        if type(i) == tuple: #въезжает кортеж
            print(*i) 
        else:  #не въезжает
            print(i) 
    print(*heap) #печатаем кучу

main()
