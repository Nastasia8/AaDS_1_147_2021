s=input().split()
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        a=stack.pop()
        b=stack.pop()
        if i=="+":
            stack.append(a+b)
        if i=="*":
            stack.append(a*b)
        if i=="-":
            stack.append(b-a)
print(*stack)
