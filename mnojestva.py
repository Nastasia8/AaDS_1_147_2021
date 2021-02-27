def func(x, y):
    result = set.intersection(x, set(y))
    if result == set():
        return(print('False'))
    else:
        return(print('True'))
func({1, 2, 3, 4, 5}, [1, 6, 7, 8, 9])