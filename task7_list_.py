#Дана целочисленная квадратная матрица. Умножить все элементы побочной диагонали на 2.
# Отобразить матрицу до преобразований и после. Создать отдельную функцию. 
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def diagonal(m):
    print("Матрица до преобразования")
    for i in range(len(matrix)):
        print(matrix[i])
    for i in range(len(matrix)):
        matrix[i][-i-1] *= 2
    print('Матрица после преобразования')
    for i in range(len(matrix)):
        print(matrix[i])

diagonal(matrix)
