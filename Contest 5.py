"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['5','-1 0 1 2 0']))  # input
>>> Function()
4
"""


def Function():
    n = int(input())
    m = 0
    Numbers = list(map(int, input().split()))

    dict = {}
    for number in Numbers:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1
            m += 1
    print(m)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
