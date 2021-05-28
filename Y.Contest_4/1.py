S = input()
stack = []
count = 0

for i in S:
    if i == ")":
        if not stack:
            count += 1
            continue
        stack.pop()
    else:
        stack.append(i)
        
print(count + len(stack))