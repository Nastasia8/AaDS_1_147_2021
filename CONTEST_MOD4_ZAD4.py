n,k = map(int, input().split())
#nums = list(map(int, input().split())) 
nums =[int(i) for i in input().split()]
stack = []
res=[0]*n
for i in range(n):
    while stack and nums[stack[-1]] > nums[i]:
        res[stack.pop()] = i
    stack.append(i)
while stack:
    res[stack.pop()]=n
minIndx = 0
for i in range(n-k+1):
    if minIndx<i:
        minIndx=i
    while res[minIndx]<i+k:
        minIndx= res[minIndx]
    print(nums[minIndx])