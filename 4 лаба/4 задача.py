
matrix=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]
def fun(matrix):
    for arr in matrix:
        for i in range(len(arr)//2):
            arr[i],arr[-i-1]=arr[-i-1],arr[i]
    return(matrix)
print(fun(matrix)



    