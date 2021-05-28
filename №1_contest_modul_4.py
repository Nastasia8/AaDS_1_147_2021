def func(m):
    stack=[]		#стек для открывающих скобок
    k=0				#кол-во всех скобок которые учавствуют в открытии/закрытии
    for i in range(len(m)):
        if (m[i]=='('):
            stack.append(m[i])
        elif (stack!=[]) and(stack[len(stack)-1]=='('): 
            stack.pop() 
        else:
            k+=1 #счетчик
    return k+len(stack)

m=input() 
print(func(m)) 