def count():
    M = int(input())
    k = input().split()[:M]
    list = set([int(x) for x in k])
    print(len(list))
    return 0


count()