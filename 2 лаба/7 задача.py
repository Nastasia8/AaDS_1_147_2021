
mat= [[1,2,3],[1,2,3],[1,2,3]]

def fun(mat):
    printmat(mat)
    for i in range(len(mat)):
        mat[i][len(mat)-i-1] *= 2
    printmat(mat)

def printmat(mat):
    for i in mat:
        for  a in i:
            print(a, end = "\t")
        print()
    print()

fun(mat)