#4.1
Q = input()
st = []
m=0
for i in Q:
    if i ==")":
        if not st or st[-1]!="(":
            m+=1
            continue
        st.pop()
    else:
        st.append(i)
print(m+len(st))
#4.2
from collections import deque
Q=int(input())
di=deque(list(map(int,input().split(maxsplit=Q))))
an=[]
am=[]
res=list(range(1,Q+1))
while di:
    if not am or am[-1]>di[0]:
        am.append(di.popleft())
    if di and am[-1]<di[0]:
        an.append(am.pop())
while am:
    an.append(am.pop())
if an==res:
    print ('YES')
else:
    print ('NO')
