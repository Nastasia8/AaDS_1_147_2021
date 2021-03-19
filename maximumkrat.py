print('x')
x = int(input())
print('y')
y = int(input())
def func(x, y):
    x = [0] * 100
    y = [0] * 100
    t = 0
    while (t - 1) != len(y):
        x.insert(t, (x * (t + 1)))
        d = 0
        while (d - 1) != len(x):
            y.insert(d, (y * (d + 1)))
            if x[t] == y[d]:
                x = [i for i in x if i != 0]
                y = [i for i in y if i != 0]
                return(x[t])
            else:
                d = d + 1
        t = t + 1

print(func(x, y))