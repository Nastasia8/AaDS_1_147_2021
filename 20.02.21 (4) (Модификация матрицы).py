matrix=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]
def func(matrix):
    for arg in matrix:
        for i in range(len(arg)//2):
            arg[i],arg[-i-1]=arg[-i-1],arg[i]

    return (matrix)

print(func(matrix))
