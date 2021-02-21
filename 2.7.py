def Multiply2(matrix):
    print("Матрица до преобразования")
    for i in range(len(matrix)):
        print(matrix[i])
    for i in range(len(matrix)):
        matrix[i][-i-1] *= 2
    print('Матрица после преобразования')
    for i in range(len(matrix)):
        print(matrix[i])

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Multiply2(matrix)
