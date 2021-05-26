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

N = int(input())
numbers = [int(i) for i in input().split()][:N]

def near_number(numbers):
    
    res = []
    
    for i in range(len(numbers)-1):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                res.append(j)
                break
            if j == len(numbers)-1:
                res.append(-1)
                
    res.append(-1)
        
    return res

print(*near_number(numbers))
