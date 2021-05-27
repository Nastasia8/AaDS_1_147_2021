s = input()
prefix = [0] * len(s) #массив для префикс функции
for i in range(len(s) - 1): #обработка префикс функции
    k = prefix[i] 
    while k > 0 and s[i + 1] != s[k]: 
        k = prefix[k - 1]
    if s[i + 1] == s[k]: prefix[i + 1] = k + 1
    else: prefix[i + 1] = 0
if (len(s) % (len(s) - prefix[-1]) == 0): print(len(s) // (len(s) - prefix[-1])) #вычисляем кол-во повторений
else: print(1) #всегда есть как минимум 1 повторение