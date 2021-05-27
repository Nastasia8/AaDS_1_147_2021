def func(Res):
    from collections import deque
    # Коллекция, благодаря которой можно работать со списком с двух сторон 
    A = deque(list(map(int,input().split())))
    B, TP = [], []
    while A:
        if not TP or TP[-1]>A[0]: 
            TP.append(A.popleft())
            # Добавление в тупик вагона из списка А
            # Удаление первого слева вагона в списке А
        if A and TP[-1]<A[0]:
            B.append(TP.pop())
            # Вагон из тупика добавляется в список В
            # Вагон из тупика удаляется
    while TP:
        B.append(TP.pop())
        # В В добавляется вагон из тупика
        # Из тупика вагон удаляется
    if B == Res:
        return('YES')
    else:
        return('NO')

N = int(input())
Res = list(range(1,N+1))
# Список создан для проверки результата
print(func(Res))
