m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def diag(m):
    print("Матрица до преобразования")
    for i in range(len(m)):
        print(m[i])
    for i in range(len(m)):
        m[i][-i-1] *= 2
    print('Матрица после преобразования')
    for i in range(len(m)):
        print(m[i])


diag(m)
