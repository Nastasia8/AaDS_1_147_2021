matrix = [[1,2,3],[1,2,3],[1,2,3]]

def m(matrix):
    printmatrix(matrix)
    for i in range(len(matrix)):
        matrix[i][len(matrix)-i-1] *= 2
    printmatrix(matrix)

def printmatrix(matrix):
    for i in matrix:
        for  a in i:
            print(a, end = "\t")
        print()
    print()
m(matrix) 