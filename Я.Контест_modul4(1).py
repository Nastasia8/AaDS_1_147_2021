def func(m):
    stack=[]
    k=0
    for i in range(len(m)):
        if (m[i]=='('): #если iый символ является (, то добавляем его в конец очереди
            stack.append(m[i])
        elif (stack!=[]) and(stack[len(stack)-1]=='('): #или стек не равен [] и проверяем след скобку, если она (, то удаляем
            stack.pop() 
        else:
            k+=1 #счетчик
    return k+len(stack)

m=input() #ввод данных
print(func(m)) #вывод функции
