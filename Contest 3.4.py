def func(n, window, nums_arr):
    stack = []
    for i in range(window):
        while stack and nums_arr[i] <= nums_arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(window, n):
        print(nums_arr[stack[0]])
        while stack and i - window >= stack[0]:
            stack.pop(0)
        while stack and nums_arr[i] <= nums_arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    print(nums_arr[stack[0]])


def main():
    n, k = map(int, input().split())
    nums_arr = list(map(int, input().split()))
    func(n, k, nums_arr)


main()
