n = int(input()) #ввод кол-ва элементов
a = list(map(int,input().split(maxsplit=n))) #ввод состава
b = [] #выезд состава
deadend = [] #тупик
while a: #пока в А что-то есть
    if not deadend or deadend[-1] > a[0]: #если в тупике ничего нет или конец тупика больше первого элемента состава
        deadend.append(a.pop(0)) #первый вагон уходит в тупик
    if a and deadend[-1] < a[0]: #если в А что-то есть и ближайший вагон тупика меньше первого элемента
        b.append(deadend.pop()) #закидываем в Б
while deadend: #если в тупике что-то осталось, то добавляем в Б
    b.append(deadend.pop())
if b == list(range(1,n+1)): #последовательность вагонов соответсвует порядку возрастания
    print("YES")
else:
    print("NO")