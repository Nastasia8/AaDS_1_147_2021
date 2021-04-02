N=input()
RA=list(map(int, input().split()))
RB=[]
stack=[]
с=1 
for i in RA:
    if i!=с:
        stack.append(i)
        continue
    RB.append(i)
    с+=1 
    for j in range(len(stack)):
        if stack[-1] == с:
            RB.append(с)
            stack.pop()
            с += 1
if RB[-1] == int(N):
    print("YES")
else:
    print("NO")
