def minimum(n, k, arr):
    stack = []
    for i in range(k):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(k, n):
        print(arr[stack[0]])
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        while stack and i - k >= stack[0]:
            stack.pop(0)
        stack.append(i)
    print(arr[stack[0]])

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    minimum(n, k, arr)

main()
