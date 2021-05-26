n = int(input()) #ввод кол-во чисел
num = list(map(int, input().split(maxsplit = n))) #вводим числа
stack = [] #стек
indexes = [-1]*n #создаём список из -1
for i in range(n-1, -1, -1): #перебираем числа с конца
    while stack and num[stack[-1]] >= num[i]: #пока стек не пустой и конец стека больше или равен числу
        stack.pop() #удаляем последнее число в стеке
    if stack: indexes[i] = stack[-1] #если стек не пустой, то индекс числа равен последнему элементу стека
    stack.append(i) #добавление рассматриваемого элемента в стек
print(*indexes) #вывод индексов 