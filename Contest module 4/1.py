n = input() #переменная принимающая значения 
stack = [] # добавляем пустой стек
k = 0      # создаем счетчик      
for i in n:
    if i == '(':
        stack.append(i) #добавляем в стек 
    elif i == ')':
        if stack:
            stack.pop() #очищаем стек
        else:
            k += 1
print(k+len(stack)) #выводим