from collections import deque
m=int(input())
v=deque(list(map(int,input().split(maxsplit=m))))
b=[]
stop=[]
res=list(range(1,m+1))
while v:
    if not stop or stop[-1]>v[0]:
        stop.append(v.popleft())
    if v and stop[-1]<v[0]:
        b.append(stop.pop())
while stop:
    b.append(stop.pop())
if b==res:
    print ('YES')
else:
    print ('NO')
    
