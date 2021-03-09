def count():
    z = int(input())
    c = input().split()[:z]
    spisok = [int(x) for x in c]

    print(len(spisok))
    return 0

count()