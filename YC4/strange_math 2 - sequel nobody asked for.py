s = input().replace(' ','')
res_s = []
stack = []
oper = {"*":3, "/":3,"+":2,"-":2,"(":1}
for i in s:
    if i in "+/*-()":
        if i == ")":
            while stack[-1][0] != "(":
                res_s.append(stack.pop()[0])
            stack.pop()
            continue
        while stack and stack[-1][1] >= oper[i] and i != "(":
            res_s.append(stack.pop()[0])
        if not stack or stack[-1][1] < oper[i] or i == "(":
            stack.append([i, oper[i]])
    else:
        res_s.append(i)
while stack:
    res_s.append(stack.pop()[0])

print(*res_s)