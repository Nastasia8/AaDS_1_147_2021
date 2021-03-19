a = int(input())
b = int(input())
def HOD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return(a+b)
print('HOD','(', a,b,') =', HOD(a,b)) 