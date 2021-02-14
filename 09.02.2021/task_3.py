def func(A, B):
    Res = set.intersection(A, set(B))
    if Res == set():
        return(print('False'))
    else:
        return(print('True'))

func({1, 2, 3, 4, 5}, [1, 6, 7, 8, 9])
