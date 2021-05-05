#Задание 1
S = input()        #о, Господи, комменты на каждой строчке(если что, то тут создаём переменную, которая будет принимать значения)()()(
stack = []         #а это - стек, он как груда книг лежащих друг на друге, но только пустой(
count = 0          #это - счётчик, может для чего-то понадобится

for i in S:                                  #ой, а это - что-то отличающееся от предыдущего, это - начало функции
    if i == ")":                             #это проверка на соотвествие элементов
        if not stack or stack[-1] != "(":    #если стек пустой или последний элемент стека не ")"
            count += 1                       #счётчик сделал +1
            continue                         #продолжаем
        stack.pop()                          #удаляем из стека( он опять пуст((( )
    else:
        stack.append(i)          #добавляем в стек (УРА, в нём что-то появилось)

print(count+len(stack))          #выводим (больше этого не повториться, а то мне надоело)


#Задание 2
from collections import deque               #если вы хотите проверить меня на знание кода, то просто напише, где комменты оставить

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
    
#Задание 3
n = int(input())
nums = list(map(int, input().split(maxsplit = n)))

d = {i:nums[i] for i in range (n)}

stack = []
index = [0] * n

for i in range(n-1, -1, -1):
    while stack and stack[-1][1] >= d[i]:
        stack.pop()
    if not stack:
        index[i] = -1
    else:
        index[i] = stack[-1][0]
    stack.append([i, d[i]])

print(*index)


#Задание 4
def min(N, K, arr):
    stack = []
    for i in range(K):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(K, N):
        print(arr[stack[0]])
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        while stack and i - K >= stack[0]:
            stack.pop(0)
        stack.append(i)
    print(arr[stack[0]])
    
def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    min(N, K, arr)
    
main()
