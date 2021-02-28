print('k')
k = int(input())
def func(k):
    res = [0] * k
    i = 0
    while k != 1:
        if k % 2 == 0:
            k = k / 2
            res.insert(i, int(k))
            i = i + 1
        else:
            k = (k * 3 + 1) / 2
            res.insert(i, int(k))
            i = i + 1
    res = [i for i in res if i != 0]
    return(res)
print(func(k))