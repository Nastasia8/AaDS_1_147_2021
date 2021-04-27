length = int(input())
a = list(zip(list(map(int, input().split())), range(length)))
stack = []
result = [0]*length
for i in reversed(a):
    while (stack != []) and (stack[-1][0] >= i[0]):
        stack.pop()
    if stack == []:
        result[i[1]] = -1
    else:
        result[i[1]] = stack[-1][1]
    stack.append(i)
print(' '.join(map(str, result))) 