s = input()
stack = []
isPop = 0
for i in s:
    if i == ')':
        if not stack or stack[-1] != '(':
            isPop += 1
            continue
        stack.pop()
    else:
        stack.append(i)

print(isPop + len(stack))  