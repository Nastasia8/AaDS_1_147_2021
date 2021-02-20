def func(a, b):
    c = a * b    
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return c // (a + b)

while 1:
    try:
        x =int(input('a = '))
        y =int(input('b = '))
        print('HOK:', func(x, y))
    except ValueError:
        break    

      