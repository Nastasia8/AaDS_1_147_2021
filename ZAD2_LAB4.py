a = int(input())
b = int(input())
def HOK(a,b):
    c = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b 
        else:
             b %= a
    return c // (a+b)
print ('NOK','(', a , b,') = ', HOK(a,b))