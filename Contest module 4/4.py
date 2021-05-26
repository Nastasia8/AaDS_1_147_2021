def min(N, K, arr): #вызываем функцию
    stack = []  #создаем пустой стек
    for i in range(K):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()  #удаляем последний элемент
        stack.append(i)
    for i in range(K, N):
        print(arr[stack[0]]) #выводим элемент списка arr
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        while stack and i - K >= stack[0]:
            stack.pop(0)
        stack.append(i) #добавляем в стек
    print(arr[stack[0]])
    
def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    min(N, K, arr)
    
main()