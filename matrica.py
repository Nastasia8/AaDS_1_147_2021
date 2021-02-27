import numpy as np

def func(x, i):
    x = np.array(x)
    n = len(x[0]) - 1
    print(x)
    while i < len(x):
        x[i][n] = x[i][n] * 2
        i += 1
        n -= 1
    print(x)
func([[3, 7, 2], [1, 4, 3], [5, 3, 2]], 0)