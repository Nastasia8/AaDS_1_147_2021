from collections import deque               

N = int(input())  # вводим количество вагонов в поезде
A = deque(list(map(int, input().split(maxsplit=N)))) #создаем очередь с установленым размером N
B = []
Toopic = []
kolvo = list(range(1, N+1))  #кол-во вагонов


while A:
    if not Toopic or Toopic[-1] > A[0]:
        Toopic.append(A.popleft()) #добавляет в Toopic первый удаленный элемент из A
    if A and Toopic[-1] < A[0]:
        B.append(Toopic.pop()) #добавляет в B последний удаленный элемент из Toopic

while Toopic:
    B.append(Toopic.pop())  #добавляет в B последний удаленный элемент из Toopic
if B == kolvo:
    print("YES")
else:
    print("NO")