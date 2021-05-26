def shift_up(cur_index, heap):
   
    while heap[cur_index] > heap[(cur_index-1)//2] and (cur_index-1)//2 >= 0:   # до тех пор пока ребенок больше родителя  ,меняем их местами
        heap[cur_index], heap[(cur_index-1) //
                              2] = heap[(cur_index-1)//2], heap[cur_index]
        cur_index = (cur_index-1)//2
    return cur_index+1  # возвращаем идекс на один больше 


def shift_down(cur_index, heap):
    while 2*cur_index+1 < len(heap):  #до тех пор пока левый индекс меньше размера куча
        left_cur_index = 2*cur_index+1
        right_cur_index = 2*cur_index+2
        child_index = left_cur_index
        
        if right_cur_index < len(heap) and heap[left_cur_index] < heap[right_cur_index]: # если правый индекс меньше размера кучи и левый элемент меньше правого
            # индекс-ребенок = правый индекс
            child_index = right_cur_index
        
        if heap[child_index] <= heap[cur_index]: # если  ребенок <= родителя - выходим из цикла 
            break
        heap[child_index], heap[cur_index] = heap[cur_index], heap[child_index]  # Меняем родителя на ребенка
        cur_index = child_index
    
    return cur_index+1 # Возвращаем индекс


def main():    
    n, m = map(int, input().split()) # Ввод данных
    result = [] # Объявляем список для вывода и самой кучи
    num = []

    for i in range(m):
        commands = list(map(int, input().split()))
        if commands[0] == 1:
            if num:
                if len(num) == 1: # Если список содержит один элемент, удаляем его и в result передаем его индекс и значение
                    x = num.pop()
                    result.append([0, x])
                else: 
                    num[0], num[-1] = num[-1], num[0]
                    x = num.pop()
                    
                    result.append([shift_down(0, num), x]) # Для вывода передаем в result список
            else:
                result.append(-1)
        
        else:
            if len(num) < n: # Проверяем дерево на кол-во элементов, если длина списка допустима добавляем элемент в дерево и поднимаем его
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
