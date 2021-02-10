def summ(slov):
    print('Словарь: ', slov)
    return(sum([value for value in slov.values()]))

def proiz(slov, res, k):
    for k in slov:
        res *= slov[k]
    return(res)
    
print('Сумма элементов = ', summ({5: 1, 2: 5, 1: 3, 3: 4, 6: 6}))
print('Произведение элементов = ', proiz({5: 1, 2: 5, 1: 3, 3: 4, 6: 6}, 1, 0))
