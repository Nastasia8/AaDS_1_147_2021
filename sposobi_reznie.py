def func_1(sp_i, sp_p, i, j):
    while i < len(sp_i):
        if sp_i[i] % 2 == 0:
            sp_p.insert(j, sp_i[i])
            j += 1
        i += 1
    return(print('Ravno: ', sorted(sp_p)))
func_1([3, 8, 2, 1, 4, 7, 5, 6, 10, 9], [], 0, 0)

#2 sposob

def func_2(sp_i, sp_p):
    sp_p = [i for i in sp_i if i % 2 == 0]
    return(print('Ravno: ', sorted(sp_p)))
func_2([3, 8, 2, 1, 4, 7, 5, 6, 10, 9], [])

#3 sposob

sp_i = [3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
sp_p = []
i = 0
j = 0

def func_3(i):
    if i % 2 == 0:
        return 1
    else:
        return 0

sp_p = filter(func_3, sp_i)
print('Ravno: ', list(sorted(sp_p)))

#4 sposob

sp_p = filter(lambda sp_i: (sp_i % 2 == 0), [3, 8, 2, 1, 4, 7, 5, 6, 10, 9])
print('Ravno: ', list(sorted(sp_p)))