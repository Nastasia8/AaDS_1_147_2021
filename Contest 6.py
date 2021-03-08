"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['5','1 50 3 4 3','16','1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5']))  # input
>>> Function()
yes
no
no
no
yes
"""


def Function():
    quantity_of_goods = int(input())
    goods = list(map(int, input().split()))
    quantity_of_orders = int(input())
    orders = list(map(int, input().split()))
    dict = {}
    for good in range(quantity_of_goods):
        dict[good+1] = goods[good]
    for order in orders:
        dict[order] += -1
    for i in range(1, quantity_of_goods+1):
        if dict[i] < 0:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
