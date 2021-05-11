#ТРЕНИРОВОЧНЫЕ ЗАДАЧИ:

#задача1
s=input()
stack=[]
isPcp=True
for i in s:
    if i==")":
        if not stack or stack [-1]!="(":
            isPcp=False
            break
        stack.pop()
    elif i=="]":
        if not stack or stack [-1]!="[":
            isPcp=False
            break
        stack.pop()
    elif i=="}":
        if not stack or stack [-1]!="{":
            isPcp=False
            break
        stack.pop()
    else:
        stack.append(i)

if isPcp and  not stack: 
    print("Yes")
else:
    print("No")

#задача2
s=input().replace(" ","")
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        d2=stack.pop()
        d1=stack.pop()
        if i == "+":
            stack.append(d1+d2)
        elif i=="*":
            stack.append(d1*d2)
        else:
            stack.append(d1-d2)

print(stack[-1])

#задача3 (сортировка фамилий)
from collections import deque
n = int(input())
q1=deque()
q2=deque()
q3=deque()
q4=deque()
for i in range(n):
    num, name = map(str,input().split())
    if int(num)==1:
        q1.append(name)
    elif int(num)==2:
        q2.append(name)
    elif int(num)==3:
        q3.append(name)
    else:
        q4.append(name)

while q1:
    print(1,q1.popleft())
while q2:
    print(2,q2.popleft())
while q3:
    print(3,q3.popleft())
while q4:
    print(4,q4.popleft())

#задача4 (пьяница)
from collections import deque

first=deque(list(map(int,input().split())))
second=deque(list(map(int,input().split())))
k=0

while k<1e6 and (len(first)*len(second)):
    first_card=first.popleft()
    second_card=second.popleft()
    if first_card == 0 and second_card == 9:
        first.append(first_card)
        first.append(second.card)
    elif first_card == 9 and second_card == 0:
        second.append(first_card)
        second.append(second_card)
    elif first_card>second_card:
        first.append(first_card)
        first.append(second_card)
    else:
        second.append(first_card)
        second.append(second_card)
    k+=1

if not first:
    print("second",k)
elif not second:
    print("first",k)
else:
    print("botva")




#ОСНОВНЫЕ ЗАДАЧИ:

#задача1
s=input()
stack=[]
a=0
for i in s:
    if i==")":
        if not stack or stack [-1]!="(":
            a+=1
            continue
        stack.pop()
    else:
        stack.append(i)
        

print(a+len(stack))



#задача2
from collections import deque
n=int(input())
a=deque(list(map(int, input().split(maxsplit=n))))
b=[]
deadlock=[]
res= list(range(1, n+1))
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



#задача3
n=int(input())
numbers=list(map(int,input().split(maxsplit=n)))
d={i:numbers[i] for i in range(n)}
stack = []
index = [0]*n
for i in range (n-1, -1, -1):
    while stack and stack[-1][1]>=d[i]:
        stack.pop()
    if not stack:
        index[i]= -1
    else:
        index[i]=stack[-1][0]
    stack.append([i,d[i]])

print(*index)



#задача4 (Евгений Сергеевич разбирал на паре)
def minimum(num, win, arr):
    stack = []
    for i in range(win):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    for i in range(win, num):
        print(arr[stack[0]])
        while stack and i - win >= stack[0]:
            stack.pop(0)
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        stack.append(i)
    print(arr[stack[0]])

n, k = map(int, input().split())
a = list(map(int, input().split()))
minimum(n, k, a)
