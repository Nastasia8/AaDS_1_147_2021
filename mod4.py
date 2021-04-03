#ТРЕНИРОВОЧНЫЕ ЗАДАЧИ:

#задача1
s=input()
stack=[]
isPcp=True
for i in s:
    if i==")":
        if not stack or stack [-1]!="(":
            isPcp=False
            break
        stack.pop()
    elif i=="]":
        if not stack or stack [-1]!="[":
            isPcp=False
            break
        stack.pop()
    elif i=="}":
        if not stack or stack [-1]!="{":
            isPcp=False
            break
        stack.pop()
    else:
        stack.append(i)

if isPcp and  not stack: 
    print("Yes")
else:
    print("No")

#задача2
s=input().replace(" ","")
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        d2=stack.pop()
        d1=stack.pop()
        if i == "+":
            stack.append(d1+d2)
        elif i=="*":
            stack.append(d1*d2)
        else:
            stack.append(d1-d2)

print(stack[-1])



#ОСНОВНЫЕ ЗАДАЧИ:

#задача1
s=input()
stack=[]
isPcp=True
a=0
for i in s:
    if i==")":
        if not stack or stack [-1]!="(":
            a+=1
            isPcp=False
            break
        stack.pop()
    else:
        stack.append(i)

print(a+len(stack))


#задача2 (я слишком тупая для неё и вообще я боюсь поезда)