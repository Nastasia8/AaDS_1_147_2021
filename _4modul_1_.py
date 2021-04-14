
S = input()
stack = []
count = 0
for item in S:
    if item ==")":
        if not stack or stack[-1]!="(":
            count+=1
            continue
        stack.pop()
    else:
        stack.append(item)
print(count+len(stack))

 
