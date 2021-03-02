
def fun():
    a = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
    in = []
    i = 0
    y = 0
    while i < len(a):
        if a[i] == 2:
             in.insert(y, i)
        y += 1
    i += 1
    print(in)

fun()