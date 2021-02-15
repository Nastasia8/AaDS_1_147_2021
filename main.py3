def main():
    a = {1, 2, 3}
    b = {2, 4, 6}
    funk(a, b)


def funk(a, b):
    if a == b:
        print (a == b)
    else:
        print(a != b)


main()

