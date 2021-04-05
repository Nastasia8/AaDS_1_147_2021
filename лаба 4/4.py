matrica1 = [[4,3,5,1],[0,7,2,9],[2,6,3,8]]
matrica2 = [[13, 97, 56],[17, 23, 85],[22,45,66]]


def funk(matrix):
    for arr in matrix:
        for i in range(len(arr)//2):
            arr[i],arr[-i-1] = arr[-i-1],arr[i]
    print(matrix)


def funk2(matrix): #немного не то
    for i in reversed(matrix):
        print(i)


def funk3(matrix):
    for i in matrix:
        for a in i:
            print(a, end = "\t")
        print()

funk(matrica1)
funk2(matrica1)
funk3(matrica1)