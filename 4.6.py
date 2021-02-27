def Function(Num):
    for i in range(len(Num)-1):
        for j in range(len(Num)-i-1):
            if Num[j] > Num[j+1]:
                Num[j], Num[j+1] = Num[j+1], Num[j]
            elif Num[j] == Num[j+1]:
                Num.remove(Num[j])
    num_tuple = tuple(Num)
    return (num_tuple)


Num = []
z = True
print("Введите число в массив или для выхода введите q")
while z == True:
    n = input()
    if (n.lower() == "q"):
        z = False
    else:
        n = float(n)
        Num.append(n)
num_tuple = Function(Num)
print(num_tuple)
