def Function(Num):
    i = 0
    while i < (len(Num) - 1):
        j = 0
        while j < len(Num) - 1 - i:
            if Num[j] > Num[j+1]:
                Num[j], Num[j+1] = Num[j+1], Num[j]
                j += 1
            elif Num[j] == Num[j+1]:
                Num.pop(j+1)

        i += 1
    num_tuple = tuple(Num)
    return (num_tuple)


Num = list(map(float, input().split()))

print(Function(Num))
