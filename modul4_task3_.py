N = int(input())
nums = list(map(int, input().split(maxsplit = N)))
d = {i:nums[i] for i in range (N)}
stack = []
index = [0] * N

for i in range(N-1, -1, -1):
    while stack and stack[-1][1] >= d[i]:
        stack.pop()
    if not stack:
        index[i] = -1
    else:
        index[i] = stack[-1][0]
    stack.append([i, d[i]])

print(*index)
