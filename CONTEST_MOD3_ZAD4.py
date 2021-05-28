s = input() #ввод
prefix = [0]*len(s) #массив для префикс функции
count = 1
for i in range(1,len(s)): #обработка префикс функции
    k = prefix[i-1] 
    while k > 0 and s[k] != s[i]: 
        k = prefix[k-1]
    if s[k] == s[i]: k += 1 
    else: k = 0 
    prefix[i] = k
    if prefix[i] < 2: count = i #пошло повторение, выводим i
print(count)