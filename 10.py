spis = [1, 20]
step1 = int(input("Первая степень: "))
step2 = int(input("Вторая степень: "))
spisupd = []


def inc(spis, step1, step2, spisupd):
    for i in range(spis[0], spis[1]):
        if i % 2 != 0:
            j = ((i ** step1) ** step2)
            spisupd.append(j)
    return spisupd


print(inc(spis, step1, step2, spisupd))
