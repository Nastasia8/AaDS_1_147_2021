import numpy as np

def func(A, i):
    A = np.array(A)
    n = len(A[0]) - 1
    print('До преобразования:\n', A)
    while i < len(A):
        A[i][n] = A[i][n] * 2
        i += 1
        n -= 1
    print('После преобразования:\n', A)
    
func([[3, 7, 2], [1, 4, 3], [5, 3, 2]], 0)
