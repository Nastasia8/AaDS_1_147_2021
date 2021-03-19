import numpy as np
def func_1(A):
    B = [0] * 2
    for i in range(0, 3):
        B.insert(i, A[i][::-1])
    B = [i for i in B if i != 0]
    A = np.array(A)
    B = np.array(B)
    return(print('Option_1:\n\n', A, '\n     🡣\n', B))
    
func_1([[4, 3, 5, 1], [0, 7, 2, 9], [2, 6, 3, 8]])
def func_2(A):
    B = [0] * 2
    for i in range(0, 3):
        B.insert(i, list(reversed(A[i])))
    B = [i for i in B if i != 0]
    A = np.array(A)
    B = np.array(B)
    return(print('\n\nOption_2:\n\n', A, '\n     🡣\n', B))
func_2([[13, 97, 56], [17, 23, 85], [22, 45, 66]])