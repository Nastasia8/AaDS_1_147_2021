n = int(input())
numbers = list(map(int, input().split(maxsplit = n)))
d = {i:numbers[i] for i in range(n)}
stack = []
index = [0]*n
for i in range(n-1, -1, -1):
    while stack and stack[-1][1] >= d[i]:
        stack.pop()
    if not stack:
        index[i] = -1
    else:
        index[i] = stack[-1][0]
    stack.append([i, d[i]])
print(*index)