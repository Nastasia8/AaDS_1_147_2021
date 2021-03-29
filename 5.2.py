s=input().split()
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        if i=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(a+b)
        if i=="*":
            a=stack.pop()
            b=stack.pop()
            stack.append(a*b)
        if i=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(b-a)
print(*stack)
