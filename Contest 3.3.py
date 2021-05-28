# Это моя версия
n = int(input())
Result = list(map(int, input().split()))
stack = [0]*(n)
minimum = min(Result)
for i in range(n):
    stack[i] = [Result[i], i]
for p in Result:
    if p == minimum:
        Result[stack[0][1]] = -1
    else:
        for i in stack:
            if p > i[0]:
                Result[stack[0][1]] = i[1]
                break
            else:
                Result[stack[0][1]] = -1
    stack.pop(0)
print(*Result)
# Ниже версия которую мы писали с Вами
# n = int(input())
# Num = list(map(int, input().split()))
# dic={i:Num[i] for i in range(n)}
# stack=[]
# index = [-1]*n
# for i in range(n-1,-1,-1):
#     while stack and stack[-1][-1]>=dic[i]:
#         stack.pop()
#     if stack:
#         index[i]= stack[-1][0]
#     stack.append([i,dic[i]])
# print(*index)
