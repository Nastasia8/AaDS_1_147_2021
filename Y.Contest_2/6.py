n = int(input())
amountOfProduct = list(map(int,input().split()))[:n]
amountOfOrders = int(input())
orders = list(map(int,input().split()))[:amountOfOrders]

for i in range(n):
    if amountOfProduct[i] < orders.count(i+1):
        print("yes")
    else:
        print("no")