from collections import deque
print ('Введите количество студентов')
m=int(input())
print ('Введите студентов №команды Фамилия')
k1=deque()
k2=deque()
k3=deque()
k4=deque()
for i in range(m):
    num,name=map(str,input().split())
    if int(num)==1:
        k1.append(name)
    elif int(num)==2:
        k2.append(name)
    elif int(num)==3:
        k3.append(name)
    else:
        k4.append(name)
while k1:
    print(1,k1.popleft())
while k2:
    print(2,k2.popleft())
while k3:
    print(3,k3.popleft())
while k4:
    print(4,k4.popleft())
