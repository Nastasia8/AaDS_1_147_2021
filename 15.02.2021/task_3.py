keys = '“Crime and Punishment”, 1, 331, 1866, “The Master and Margarita”, '\
       '1, 470, 1966, “War and Peace”, 4, 1274, 1869, “And Quiet Flows the Don”, '\
       '4, 1600, 1940'.split(', ')

def func(keys, znach):
    n = -1
    k = -1

    while n > -len(keys):
        znach[k] = keys[n-2].split() + keys[n-1].split() + keys[n].split()
        k -= 1
        n -= 4
    
    k = 1

    while len(keys) != 4:
        del keys[k:k+3]
        k += 1
    
    res = dict(zip(keys, znach))
    return(res)

print(func(keys, [0] * 4))
