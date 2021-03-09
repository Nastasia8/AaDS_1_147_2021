def count():
    a = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
    b = []
    i = 0
    for item in a:
        if item == 2:
                b.append(i)
        i+=1
    print(b)
count()