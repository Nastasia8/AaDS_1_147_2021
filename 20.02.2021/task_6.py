print('Введите колличество чисел в списке: ', end='')
k = int(input())

def fillsin(spis):
    i = 1
    while i <= k:
        print('Введите ', i, ' число: ', end='')
        spis[i-1] = int(input())
        i = i + 1
    return(set(spis))

def func(spis):
    spis = tuple(spis)
    return(print(spis))
    
func(fillsin([0] * k))
