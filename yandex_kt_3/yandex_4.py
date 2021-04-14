def prefix(S): 
    P = [0] * len(S) 
    for i in range(len(S)-1): 
        k = P[i] 
        while k > 0 and S[i+1] != S[k]: 
            k = P[k-1]
        if S[i+1] == S[k]:
            P[i+1] = k + 1
        else:
           P[i+1] = 0
    return(P)

S = str(input()) 
S_S = S + '$' + S #Складываем (конкатинируем) строки через символ '$'
P = prefix(S_S) #Вызываем функцию и присваиваем значению P её результат
pr = P[-1] - P[len(S)-1] #Вычисляем значение, на которое поделим строку
print(pr) 
