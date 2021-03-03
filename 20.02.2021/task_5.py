def func(spis):
    spis = spis.split(', ')
    n = len(spis)
    i = -1
    while i > -n:
        j = i - 1
        hh = spis[i]
        while j > -n:
            if hh == spis[j]:
                spis[i] = str(spis[i]) + str(hh)
            j = j - 1
        i = i - 1
    return(print(set(spis)))
    
func('1, 7, 4, 7, 15, 4, 7, 5, 2')
