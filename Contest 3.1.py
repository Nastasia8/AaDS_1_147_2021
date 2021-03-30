s = '))((('  # input()
stack = []
is_p_c_p = 0
for i in s:
    if i == ')':
        if not stack or stack[-1] != '(':
            is_p_c_p += 1
            continue
        stack.pop()
    else:
        stack.append(i)
print(is_p_c_p+len(stack))
if is_p_c_p and not stack:
    print("Yes")
else:
    print("None")
