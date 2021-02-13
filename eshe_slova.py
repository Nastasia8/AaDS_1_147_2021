def summ(slova):
    print('Slova', slova)
    return(sum([value for value in slova.values()]))

def proiz(slova, result, k):
    for k in slova:
        result *= slova[k]
    return(result)
    
print(summ({5: 1, 2: 5, 1: 3, 3: 4, 6: 6}))
print(proiz({5: 1, 2: 5, 1: 3, 3: 4, 6: 6}, 1, 0))