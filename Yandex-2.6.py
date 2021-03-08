def fun():
    inWarehouse = int(input())
    seen = list(map(int, input().split()))
    general = int(input())
    orders = list(map(int, input().split()))
    
    spis = {}

    for item1 in range(inWarehouse):
        spis[item1+1] = seen[item1]
    for item2 in orders:
        spis[item2] += -1
    for i in range(1, inWarehouse+1):
        if spis[i] < 0:
            print("yes")
        else:
            print("no")

fun()

