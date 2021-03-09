print('Введите первое число: ', end='')
x = int(input())
print('Введите второе число: ', end='')
y = int(input())

def func(x, y):
    xlist = [0] * 100
    ylist = [0] * 100
    t = 0
    while (t - 1) != len(ylist):
        xlist.insert(t, (x * (t + 1)))
        d = 0
        while (d - 1) != len(xlist):
            ylist.insert(d, (y * (d + 1)))
            if xlist[t] == ylist[d]:
                xlist = [i for i in xlist if i != 0]
                ylist = [i for i in ylist if i != 0]
                return(xlist[t])
            else:
                d = d + 1
        t = t + 1

print('НОК(', x, ';', y, ') = ', func(x, y))

