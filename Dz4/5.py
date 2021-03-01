a = [1,7,4,7,15,4,7,5,2]

def func(a):
    for i in range(len(a)):
        k = a.count(a[i])
        if k>1:
            a[i] = str(a[i])*k
    return set(a)
print(func(a))