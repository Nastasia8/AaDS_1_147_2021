def minimum(num, win, arr): #Евгений Сергеевич помог на паре, разбирали
    stack = []
    for i in range(win):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(win, num):
        print(arr[stack[0]])
        while stack and i - win >= stack[0]:
            stack.pop(0)
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    print(arr[stack[0]])

n, k = map(int, input().split())
a = list(map(int, input().split()))
minimum(n, k, a)