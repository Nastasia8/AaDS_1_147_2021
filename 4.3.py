def Function(N, Intermediate_result):
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = (N*3 + 1)//2
        Intermediate_result.append(N)


N = int(input("Введите натуральное число:"))
Intermediate_result = [N]
Function(N, Intermediate_result)
for i in range(0, len(Intermediate_result)):
    print(Intermediate_result[i], end=" ")
