
def funk(prod, ord, numpad):
    for i in range(numprod):
        if products[i] < orders.count(i + 1):
            print("yes")
        else:
            print("no")

numprod = int(input())
products = list(map(int,input().split()))[:numprod]
numorders = int(input())
orders = list(map(int,input().split()))[:numorders]
funk(products, orders, numprod)