def count():
    Q = int(input())
    t = input().split()[:Q]
    spis = [int(x) for x in t]

    print(len(spis))
    return 0

count()