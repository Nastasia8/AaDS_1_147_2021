keys = '“Crime and Punishment”, 1, 331, 1866, “The Master and Margarita”,'1, 470, 1966, “War and Peace”, 4, 1274, 1869, “And Quiet Flows the Don”,'4, 1600, 1940'
def func(keys, x):
    n = -1
    k = -1

    while n > -len(keys):
        x[k] = keys[n-2] + keys[n-1] + keys[n]
        k -= 1
        n -= 4
        
    k = 1

    while len(keys) != 4:
        del keys[k:k+3]
        k += 1

    result = dict(zip(keys, x))
    return(result)
print(func(keys, [0] * 4))