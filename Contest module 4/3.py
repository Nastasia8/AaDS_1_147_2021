N = int(input()) #  количество элементов в массиве
n = list(map(int, input().split(maxsplit = N))) #создаем очередь с установленым размером N
stack = []
index = [0]*N
for i in range(N-1, -1, -1):
    while stack and n[stack[-1]] >= n[i]:
        stack.pop() #удаляем последний элемент в стеке
    index[i] = stack[-1] if stack else -1  # если есть ближайшее справа строго меньшего числа,то выводим,иначе -1
    stack.append(i) #добавляем в стек

print(*index)