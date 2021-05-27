from collections import deque
n = int(input())
q1 = deque()
q2 = deque()
for i in range(n):
    num, name = map(str, input().split())
    if int(num) == 1:
        q1.append(name)
    else:
        q2.append(name)

while q1:
    print(1, q1.popleft())
while q2:
    print(2, q2.popleft())    