S = input()
stack = []
k = 0

for i in range(0, len(S)):
    if S[i] == '(':
        stack.append(S[i]) #Добавляем в стек символ '('
    elif stack!=[] and stack[len(stack)-1] == '(':
        stack.pop() #Удаляем последний символ из стека
    else:
        k += 1
        
print(k + len(stack))
