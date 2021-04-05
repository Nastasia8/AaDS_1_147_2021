n = int(input())
Result = list(map(int, input().split()))
stack=[0]*(n)
for i in range(n):
    stack[i]= [Result[i],i]
minimum=min(Result)
for p in Result:
    if p==minimum:
        Result[stack[0][1]]=-1
    else:
        for i in stack:
            if p> i[0]:
                Result[stack[0][1]]=i[1]
                break
    stack.pop(0)
print(*Result)
        


