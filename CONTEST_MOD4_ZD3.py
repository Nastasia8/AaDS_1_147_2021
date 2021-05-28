def find(arr, j):
    stack = [j - 1]
    a = [0] * j
    a[j - 1] = -1
    for i in range(j - 2, -1, -1):
        if arr[i] <= arr[stack[-1]]:
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                a[i] = -1
            else:
                a[i] = stack[-1]
            stack.append(i)
        else:
            a[i] = stack[-1]
            stack.append(i)
    return a
j = int(input())
arr = list(map(int, input().split()))
arr = find(arr, j)
print(' '.join(map(str, arr)))