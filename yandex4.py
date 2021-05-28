#1

S = input()
stack = []
count = 0

for i in S:
    if i == ")":
        if not stack:
            count += 1
            continue
        stack.pop()
    else:
        stack.append(i)
        
print(count + len(stack))

#2

from collections import deque

N = int(input())
A = deque(list(map(int, input().split(maxsplit=N))))
B = []
Deadlock = []
res = list(range(1, N+1))

while A:
    if not Deadlock or Deadlock[-1] > A[0]:
        Deadlock.append(A.popleft())
    if A and Deadlock[-1] < A[0]:
        B.append(Deadlock.pop())

while Deadlock:
    B.append(Deadlock.pop())
if B == res:
    print("YES")
else:
    print("NO")
    
#3


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
