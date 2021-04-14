n, k = map(int, input().split())
Numbers = list(map(int, input().split()))
stack = Numbers[:(k-1)]
Numbers = Numbers[k-1:]
Min = min(stack)
for i in range(n-k+1):
    stack.append(Numbers.pop(0))
    if Min <= stack[-1] and Min != stack[0]:
        print(Min)
    elif Min <= stack[-1]:
        print(Min)
        stack.pop(0)
        Min = min(stack)
        continue
    else:
        Min = stack[-1]
        print(Min)
    stack.pop(0)
