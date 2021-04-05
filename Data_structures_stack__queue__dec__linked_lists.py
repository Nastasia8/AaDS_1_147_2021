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