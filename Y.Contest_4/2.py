from collections import deque

n = int(input())
a = deque(list(map(int, input().split(maxsplit = n))))
b = []
deadlock = []
res = list(range(1, n+1))

while a:
    if not deadlock or deadlock[-1] > a[0]:
        deadlock.append(a.popleft())
    if a and deadlock[-1] < a[0]:
        b.append(deadlock.pop())

while deadlock:
    b.append(deadlock.pop())
if b == res:
    print("YES")
else:
    print("NO")