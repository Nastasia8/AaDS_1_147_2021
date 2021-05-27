def func(N, arr):
    stack = []
    # Создание стека
    index = [-1]*N
    # Создание списка из -1
    for i in range(N-1, -1, -1):
        # Цикл перебора чисел с конца
        while stack and arr[stack[-1]] >= arr[i]: 
            stack.pop()
            # Удаляем последнее число из стека
        if stack: index[i] = stack[-1] 
        stack.append(i)
        # Добавляем в стек элемент i
    return(index)

N = int(input()) 
arr = list(map(int, input().split()))
print(*func(N, arr))
