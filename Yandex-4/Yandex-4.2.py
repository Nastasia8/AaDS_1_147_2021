from collections import deque
n = int(input())
a = deque(list(map(int, input().split(maxsplit=n))))
b = []
deadblock = []
res = list(range(1, n + 1))
while a:
    if not deadblock or deadblock[-1] > a[0]:
        deadblock.append(a.popleft())
    if a and deadblock[-1] < a[0]:
        b.append(deadblock.pop())

while deadblock:
    b.append(deadblock.pop())
if b == res:
    print('YES')
else:
    print('NO')