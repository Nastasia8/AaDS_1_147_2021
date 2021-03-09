def Function(Num):
    i = 0
    while i < (len(Num) - 1):
        j = 0
        while j < len(Num) - 1:
            if Num[j] > Num[j+1]:
                Num[j], Num[j+1] = Num[j+1], Num[j]
                j -= 1
            elif Num[j] == Num[j+1]:
                Num.pop(j)
            j += 1
        i += 1

    for i in range(len(Num)):
        if (Num[i]*10) % 10 == 0:
            Num[i] = int(Num[i])

    return tuple(Num)


Num = list(map(float, input().split()))
num_tuple = Function(Num)
print(*num_tuple, end=" ")
