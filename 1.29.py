s = input()
stack = []
isPop = True
for i in s:
    if i == ')':
        if not stack or stack[-1] != "(":
            isPop = False
            break
        stack.pop()
    elif i == ']':
        if not stack or stack[-1] != '[':
            isPop = False
            break
        stack.pop()
    elif i == '}':
        if not stack or stack[-1] != '{':
            isPop = False
            break
        stack.pop()
    else:
        stack.append(i)
if isPop and not stack:
    print('Yes')
else:
    print('No')                    