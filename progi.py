def func(result):
    print('1')
    x = int(input())
    print('2')
    y = int(input())
    while x <= y:
        if x % 2 == 0:
            result += x
            x += 2
        else:
            x += 1
    return(result)
print(func(result = 0))