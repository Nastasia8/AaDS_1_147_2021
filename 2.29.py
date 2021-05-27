stack = []
for i in input().split():
    if not i.isdigit():
        a = stack.pop()
        b = stack.pop()
        # stack.pop()
        # stack.pop()
        if i == "+":
            result = a + b
        elif i == "-":
            result = a - b
        else:
            result = a * b
        stack.append(result)
    else:
        stack.append(int(i))

print(*stack)
