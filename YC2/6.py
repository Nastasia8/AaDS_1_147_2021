articles = int(input())
article_amount = list(map(int,input().split()))[:articles]

clients = int(input())
client_orders = list(map(int,input().split()))[:clients]

for i in range(articles):
    if article_amount[i] < client_orders.count(i + 1):
        print('yes')
    else: 
        print('no')





