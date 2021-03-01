a=[3, 8, 2, 1, 4, 7, 5, 6, 10, 9]
b=[3, 9, 2, 1, 8, 7, 4, 10, 6]
def func(a=set(),b=[]):
    if a==b:
        return True
    else:
        return False
print(func(a,b))