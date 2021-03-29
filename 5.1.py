s=input()
stack=[]
is_p_c_p=True
for i in s:
    if i ==')':
        if not stack or stack[-1]!='(':
            is_p_c_p=False
            break
        stack.pop()
    elif i ==']':
        if not stack or stack[-1]!='[':
            is_p_c_p=False
            break
        stack.pop()
    elif i =='}':
        if not stack or stack[-1]!='{':
            is_p_c_p=False
            break
        stack.pop()
    else:
        stack.append(i)
if is_p_c_p and not stack:
    print("Yes")
else:
    print("None")