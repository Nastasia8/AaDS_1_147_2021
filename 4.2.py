def NOK(x, y):
    c = x*y
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return c//(x+y)


x = int(input("x="))
y = int(input("y="))
n = NOK(x, y)
print("NOK({0};{1}) = {2}".format(x, y, n))
