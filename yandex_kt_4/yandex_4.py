def func(N, K, Array, stack):
    for i in range(N):
        while stack and Array[i] <= Array[stack[-1]]: 
            stack.pop()
            # Удаляем число из стека
        while stack and i - K >= stack[0]:
            stack.pop(0)
            # Удаляем число из стека
        stack.append(i)
        # Добавляем в стек i
        if i>=K-1: print(Array[stack[0]])


N, K = map(int, input().split())
Array = list(map(int, input().split()))
func(N, K, Array, [])
